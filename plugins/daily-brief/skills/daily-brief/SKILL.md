---
name: daily-brief
description: |-
  Generate a daily briefing dashboard from calendar, unread email, recent Slack activity,
  new Jira backlog items, team demos, and community forum activity. Shows today's
  meeting schedule, scans Gmail inbox and Slack channels, lists new Jira issues created
  since the last business day, surfaces demos posted by direct reports, checks an optional
  community forum for new posts, triages items by urgency (Immediate Action, Needs Response,
  FYI), deduplicates cross-source items, and writes the dashboard to a configurable path.
  Use when asked for "daily brief", "morning brief", "what did I miss", "catch me up",
  or invoke with /daily-brief.
user-invocable: true
---

# Daily Brief

Generate a morning briefing dashboard covering today's calendar, unread email, recent Slack activity, new Jira backlog items, and community forum activity.

## Execution Flow

### Step 0: Load configuration

Read the config file at `.claude/daily-brief.yaml` (relative to the current working directory).

If the file does not exist, stop immediately and tell the user:

> Configuration file not found at `.claude/daily-brief.yaml`.
> Copy the example config from the plugin directory and fill in your values:
> `cp ~/.claude/plugins/cache/*/daily-brief/config.example.yaml .claude/daily-brief.yaml`

Parse the YAML config. Extract these values (all sections are optional unless noted):

- `team.members` — list of team members with `name` and `slack_display_name`
- `team.roster_file` — if set, read the external YAML file. When reading `roster_file`, look for team members in this order:
  1. Top-level `members` list (flat format)
  2. `teams[0].members` (team roster format, e.g., pdt.yaml)
  
  Use whichever is found first. Each member entry must have `name` and `slack_display_name` fields. Use the roster file members instead of (or merged with) inline members.
- `slack.team_channels` — list of `{id, name}` objects
- `slack.org_channels` — list of `{id, name}` objects
- `slack.demos_channel` — single `{id, name}` object
- `jira.backlog_filter_id` — Jira saved filter ID string
- `jira.escalation_label` — label string for flagging escalations
- `forum.enabled` — boolean
- `forum.url` — Discourse tag JSON endpoint URL
- `forum.tag` — tag name for display

Derive the forum base URL from `forum.url` by stripping the path (e.g., `https://forum.ansible.com/tag/jewel/514.json` → `https://forum.ansible.com`). Store this as `forum_base_url` for use in topic links.
- `timezone` — IANA timezone name (default: `America/New_York`). Used for cutoff calculations and display timestamps. Derive the UTC offset (`<timezone_offset>`, e.g., `-04:00`) and abbreviation (`<timezone_abbrev>`, e.g., `EDT`) from this value for use in subagent prompts and the dashboard. Pass the timezone to compute-lookback.sh as the second argument.
- `output.dashboard_path` — where to write the dashboard (default: `Dashboards/daily-brief.md`)
- `output.state_path` — where to read/write state (default: `Dashboards/snapshots/daily-brief-state.json`)

Then discover the user's Slack identity by calling `mcp__mcp-slack__whoami`. Extract the user's display name and user ID. These replace all hardcoded references to the user in subagent prompts (for self-message filtering and `to:me` searches).

Also extract the Slack workspace URL from the `whoami` response (typically in the format `https://<workspace>.slack.com`). If not directly available, construct it from the team domain. This URL is used for hyperlinking Slack channels in the dashboard.

For Jira URLs, the instance URL can be discovered by:
- Reading the JIRA_URL environment variable from the mcp-atlassian server configuration, OR
- Extracting the base URL from any Jira API response (e.g., from a `jira_search` result, the issue `self` URL will be `https://<instance>.atlassian.net/rest/api/2/issue/...`)

Store these URLs for use in dashboard link formatting (Step 5).

### Step 1: Determine time window

Run the lookback computation script to get all timestamps:

```bash
bash <plugin-dir>/skills/daily-brief/scripts/compute-lookback.sh "<output.state_path>" "<timezone>"
```

Where `<plugin-dir>` is the plugin's install directory (the skill system provides this as the skill's base directory), `<output.state_path>` is the value from config, and `<timezone>` is the IANA timezone (default: `America/New_York`).

The script outputs JSON with these fields:
- `today` — today's date (YYYY-MM-DD), used for calendar queries
- `prev_biz_day` — previous business day (YYYY-MM-DD), used in the dashboard header and Slack/Jira queries
- `cutoff_unix` — Unix timestamp for 5:00 PM <timezone> on the previous business day, used as the Slack `oldest` parameter and Jira `created >=` filter
- `current_unix` / `current_iso` / `current_time` — current timestamps for the dashboard header and state file
- `timezone` / `timezone_abbrev` — the configured timezone name and abbreviation (e.g., `America/New_York` / `EDT`)
- `demos_lookback_unix` / `demos_lookback_iso` — demos lookback from the state file (or 24h fallback), used ONLY by the demos subagent (Step 2g)

**Do not manually calculate dates or day-of-week.** Use the script output directly. Parse the JSON and substitute the values into the subagent prompts below.

Email scanning uses no time window — it scans all unread messages regardless of age.

### Step 2: Dispatch data-gathering subagents in parallel

Dispatch subagents based on which config sections are present. Always dispatch these:

- 2a: Email subagent (requires Google Workspace MCP)
- 2b: Slack DMs/Mentions subagent (requires Slack MCP)
- 2e: Calendar subagent (requires Google Workspace MCP)

Conditionally dispatch these:

- 2c: Slack Team Channels — only if `slack.team_channels` is present and non-empty
- 2d: Slack Org Channels — only if `slack.org_channels` is present and non-empty
- 2f: Jira backlog — only if `jira` section is present in config
- 2g: Demos — only if `slack.demos_channel` is present AND `team.members` is non-empty
- 2h: Community Forum — only if `forum.enabled` is true

Dispatch all applicable subagents in parallel using the Agent tool. All must be in a single message to ensure parallel execution. The exact count depends on channel splitting (see 2c and 2d below) — typically 11-13 subagents.

**All data-gathering subagents must use `model: "haiku"`** — they perform mechanical API calls, filtering, and formatting that don't require advanced reasoning. The parent orchestrator (Opus) handles triage, deduplication, and dashboard writing where judgment matters.

#### 2a: Email subagent

Use `subagent_type: general-purpose` with this prompt:

```text
Scan unread Gmail messages and return a triaged summary.

Steps:
1. Call mcp__google-workspace__search_gmail_messages with:
   - query: "is:unread in:inbox"
   - page_size: 25
   - user_google_email: <user's Google Workspace email from MCP config>

2. If results are returned, collect all message IDs.

3. Fetch metadata in batches of 25 using mcp__google-workspace__get_gmail_messages_content_batch with:
   - format: "metadata"
   - user_google_email: <user's Google Workspace email from MCP config>

4. If the search returned more than 25 results, use the next_page_token to fetch additional pages and repeat the metadata fetch for each batch.

5. For each message, extract: From (sender name and email), Subject, Date.

6. Classify each message with an urgency signal based on these rules:

   IMMEDIATE — any of these patterns:
   - Subject contains "Your Action Required", "Complete Manager Evaluation", "A To-Do Awaits"
   - From: redhat@myworkday.com with action-oriented subject
   - Subject contains "Concur Alert" or "Outstanding" (expense deadlines)
   - Subject contains "Proposed new time" for today's date (calendar reschedule needed today)
   - From: jira with escalation-related content

   RESPONSE_NEEDED — any of these patterns:
   - Subject starts with "Proposed new time" (for future dates)
   - Subject starts with "Declined:" (calendar — may need to reschedule)
   - Direct email from a person (not a mailing list, not automated) — check for Precedence: list or List-Id headers to identify mailing lists
   - Subject starts with "Invitation:" (calendar invite needing RSVP)

   FYI — everything else:
   - Has List-Id or Precedence: list/bulk headers (mailing lists)
   - From automated senders (jira@, jenkins, bot, noreply, alerts@)
   - Subject starts with "Canceled event" (informational)
   - Subject contains "Friday Five", "This Week in", "Newsletter"

7. Return the total count of unread messages and a structured list in this exact format, one per line:

URGENCY | SENDER_NAME | SUBJECT | DATE | REASON

Where URGENCY is one of: IMMEDIATE, RESPONSE_NEEDED, FYI

Sort by urgency (IMMEDIATE first, then RESPONSE_NEEDED, then FYI), then by date descending within each group.
```

#### 2b: Slack DMs/Mentions subagent

Use `subagent_type: general-purpose` with this prompt (substitute actual values for the placeholders):

```text
Scan Slack for DMs and @mentions relevant to <user's Slack display name> and return a filtered summary.

Scanning since: [PREVIOUS_BUSINESS_DAY_DATE] 5:00 PM <timezone> (Unix timestamp: [UNIX_TIMESTAMP])

Run these two searches in parallel using mcp__mcp-slack__search_messages:
1. Search: "to:me after:[PREVIOUS_BUSINESS_DAY_DATE]" with limit: 50, sort: "timestamp"
2. Search: "@<user's Slack handle> after:[PREVIOUS_BUSINESS_DAY_DATE]" with limit: 50, sort: "timestamp"

Deduplicate results that appear in both searches (match on timestamp).
After deduplication, discard any messages with a timestamp before [UNIX_TIMESTAMP] (5:00 PM <timezone> on [PREVIOUS_BUSINESS_DAY_DATE]).

## Filtering

- EXCLUDE messages authored by <user's Slack display name>
- EXCLUDE bot-only messages that have zero human replies in their thread. A bot message IS included if any human replied to it.
- INCLUDE everything else

## Output Format

### DMs and Mentions
For each item: AUTHOR | TIMESTAMP | MESSAGE_SNIPPET (first 200 chars) | MENTIONS_USER: yes/no

Also return: DMs/mentions count: [N]

Do NOT triage or categorize — just return the filtered feed.
```

#### 2c: Slack Team Channels subagents (split for speed)

Use the `slack.team_channels` list from the config.

**Split the team channel list into groups of no more than 3 channels each.** Dispatch one subagent per group (e.g., 7 channels → 3 subagents of 3, 2, 2). Each subagent uses `subagent_type: general-purpose` with this prompt template, substituting only that group's channels:

```text
Fetch recent Slack messages from team channels and return a filtered summary.

Scanning since: [PREVIOUS_BUSINESS_DAY_DATE] 5:00 PM <timezone> (Unix timestamp: [UNIX_TIMESTAMP])

Fetch channels ONE AT A TIME (do NOT fetch in parallel). For each channel:
1. Call mcp__mcp-slack__get_channel_history with oldest: "[UNIX_TIMESTAMP]", limit: 50, include_threads: true
2. IMMEDIATELY write the output for that channel before fetching the next one
3. Every message from this fetch belongs to THIS channel — do not re-attribute messages later

This sequential approach is CRITICAL. Fetching channels in parallel causes message misattribution.

Channels to fetch:
[LIST ONLY THIS GROUP'S CHANNELS AS: - CHANNEL_ID (CHANNEL_NAME)]

## Filtering

- EXCLUDE messages authored by <user's Slack display name>
- EXCLUDE bot-only messages that have zero human replies in their thread. A bot message IS included if any human replied to it.
- INCLUDE everything else

## Output Format

### Team Channels
For each channel with activity, group messages under the channel ID and name:
CHANNEL_ID | CHANNEL_NAME:
- AUTHOR | CHANNEL_ID | TIMESTAMP | MESSAGE_SNIPPET (first 200 chars) | MENTIONS_USER: yes/no | IS_THREAD_REPLY: yes/no

If a channel had no activity (after filtering), report: "CHANNEL_ID | CHANNEL_NAME: No activity"

CRITICAL: A message MUST be listed under the channel it was fetched from. Never move a message to a different channel section.

Also return: Team channel message count: [N]

Do NOT triage or categorize — just return the filtered feed.
```

#### 2d: Slack Org Channels subagents (split for speed)

Use the `slack.org_channels` list from the config.

**Split the org channel list into groups of no more than 3 channels each.** Dispatch one subagent per group (e.g., 8 channels → 3 subagents of 3, 3, 2). Each subagent uses `subagent_type: general-purpose` with this prompt template, substituting only that group's channels:

```text
Fetch recent Slack messages from organization channels and return a filtered summary.

Scanning since: [PREVIOUS_BUSINESS_DAY_DATE] 5:00 PM <timezone> (Unix timestamp: [UNIX_TIMESTAMP])

Fetch channels ONE AT A TIME (do NOT fetch in parallel). For each channel:
1. Call mcp__mcp-slack__get_channel_history with oldest: "[UNIX_TIMESTAMP]", limit: 50, include_threads: true
2. IMMEDIATELY write the output for that channel before fetching the next one
3. Every message from this fetch belongs to THIS channel — do not re-attribute messages later

This sequential approach is CRITICAL. Fetching channels in parallel causes message misattribution.

Channels to fetch:
[LIST ONLY THIS GROUP'S CHANNELS AS: - CHANNEL_ID (CHANNEL_NAME)]

## Filtering

- EXCLUDE messages authored by <user's Slack display name>
- EXCLUDE bot-only messages that have zero human replies in their thread. A bot message IS included if any human replied to it.
- INCLUDE everything else

## Output Format

### Org Channels
For each channel with activity, group messages under the channel ID and name:
CHANNEL_ID | CHANNEL_NAME:
- AUTHOR | CHANNEL_ID | TIMESTAMP | MESSAGE_SNIPPET (first 200 chars) | MENTIONS_USER: yes/no | IS_THREAD_REPLY: yes/no

If a channel had no activity (after filtering), report: "CHANNEL_ID | CHANNEL_NAME: No activity"

CRITICAL: A message MUST be listed under the channel it was fetched from. Never move a message to a different channel section.

Also return: Org channel message count: [N]

Do NOT triage or categorize — just return the filtered feed.
```

#### 2e: Calendar subagent

Use `subagent_type: general-purpose` with this prompt (substitute today's date for the placeholder):

```text
Fetch today's calendar events for the user and return a structured schedule.

Steps:
1. Call mcp__google-workspace__get_events with:
   - calendar_id: "primary"
   - time_min: "[TODAY_DATE]T00:00:00<timezone_offset>"
   - time_max: "[TODAY_DATE]T23:59:59<timezone_offset>"
   - max_results: 50
   - detailed: true
   - user_google_email: <user's Google Workspace email from MCP config>

2. Filter the results:
   - EXCLUDE all-day events (events with a date but no dateTime in start/end)
   - EXCLUDE events where the title contains "Focus time" or "Focus Time" (case-insensitive)
   - EXCLUDE events the user has declined (responseStatus: "declined")
   - INCLUDE everything else

3. For each remaining event, extract:
   - Start time (converted to the configured timezone, formatted as h:MM AM/PM)
   - End time (converted to the configured timezone, formatted as h:MM AM/PM)
   - Duration in minutes
   - Title (summary)
   - Whether it's recurring (recurringEventId is present)
   - User's response status (accepted, tentative, needsAction)

4. Sort by start time ascending.

5. Flag scheduling notes:
   - Back-to-back: if less than 5 minutes gap between one event's end and the next event's start
   - Conflict: if two events overlap in time

6. Return the results in this exact format, one per line:

START_TIME | END_TIME | DURATION_MIN | TITLE | RECURRING: yes/no | STATUS: accepted/tentative/needsAction

After the event list, add a line:
TOTAL_MEETINGS: [count]

If there are back-to-back or conflicting events, add:
SCHEDULING_NOTES:
- BACK_TO_BACK: [event1 title] → [event2 title] (no gap)
- CONFLICT: [event1 title] overlaps [event2 title]
```

#### 2f: Jira backlog subagent

Use `jira.backlog_filter_id` and `jira.escalation_label` from the config.

Use `subagent_type: ansible-jira-expert:jira-operator` with this prompt (substitute actual values for the placeholders):

```text
Search for new Jira issues and return a structured list.

Steps:
1. Call jira_search with this JQL:
   filter=<jira.backlog_filter_id> AND created >= "[PREVIOUS_BUSINESS_DAY_DATE] 17:00"

   Set max_results to 50.

2. For each issue returned, extract:
   - Issue key (e.g., AAP-12345)
   - Issue type (Bug, Story, Task, etc.)
   - Priority (Critical, Major, Normal, Minor, etc.)
   - Summary (title)
   - Reporter (display name)
   - Labels (list of labels on the issue)
   - Created date

3. Sort by priority (Critical first, then Blocker, Major, Normal, Minor), then by created date descending.

4. Return the results in this exact format, one per line:

ISSUE_KEY | TYPE | PRIORITY | SUMMARY | REPORTER | LABELS | CREATED_DATE

After the list, add:
TOTAL_NEW_ISSUES: [count]

If there are issues with the label "<jira.escalation_label>", flag them:
ESCALATIONS: [comma-separated list of issue keys with <jira.escalation_label> label]

If there are issues with Critical or Blocker priority, flag them:
HIGH_PRIORITY: [comma-separated list of issue keys with Critical or Blocker priority]

If no issues are found, return:
TOTAL_NEW_ISSUES: 0
```

#### 2g: Demos subagent

Use `team.members[*].slack_display_name` from the config for the author filter and `slack.demos_channel.id` for the channel ID.

Use `subagent_type: general-purpose` with this prompt (substitute actual values for the placeholders):

```text
Fetch recent demos posted by team members in the demos channel and return a structured list.

Steps:
1. Call mcp__mcp-slack__get_channel_history with:
   - channel: "<slack.demos_channel.id>"
   - oldest: "[DEMOS_LOOKBACK_UNIX_TIMESTAMP]"
   - limit: 50
   - include_threads: true

2. Filter the results to ONLY messages authored by these team members (match on Slack display name):
   [LIST EACH MEMBER AS: - DISPLAY_NAME]

   Discard all messages from authors not in this list.

3. From the remaining messages, extract:
   - Author (Slack display name)
   - Timestamp
   - Message text (first 300 chars)
   - Any URLs in the message (video links, recording links, PR links, etc.)
   - Thread reply count (if available)

4. Sort by timestamp descending (newest first).

5. Return the results in this exact format, one per line:

AUTHOR | TIMESTAMP | MESSAGE_SNIPPET | URLS | THREAD_REPLIES

After the list, add:
TOTAL_DEMOS: [count]

If no messages from team members are found, return:
TOTAL_DEMOS: 0
```

#### 2h: Community Forum subagent

Use `subagent_type: general-purpose` with this prompt (substitute actual values for the placeholders):

```text
Check the community forum for new activity on <forum.tag>-tagged posts and return a structured summary.

Steps:
1. Use WebFetch to fetch <forum.url> with prompt: "Return the complete topic_list.topics array with all fields for each topic, especially: id, title, slug, posts_count, reply_count, views, created_at, last_posted_at, last_poster_username, and the posters array."

2. From the response, examine each topic's last_posted_at timestamp. Filter to only topics where last_posted_at is after [PREVIOUS_BUSINESS_DAY_DATE]T21:00:00Z (5:00 PM <timezone>).

3. Also check for brand new topics: any topic where created_at is after [PREVIOUS_BUSINESS_DAY_DATE]T21:00:00Z.

4. For each topic with new activity, fetch the individual topic to find new posts:
   Use WebFetch on <forum_base_url>/t/[SLUG]/[ID].json with prompt: "Return all posts in the post_stream.posts array. For each post, include: post_number, username, created_at, and the first 300 characters of the cooked field (HTML content)."

   Filter the returned posts to only those with created_at after [PREVIOUS_BUSINESS_DAY_DATE]T21:00:00Z.

5. Return results in this format:

For each topic with new activity:
TOPIC_TITLE | TOPIC_URL: <forum_base_url>/t/[SLUG]/[ID] | TOTAL_POSTS | VIEWS | NEW_POSTS_COUNT | IS_NEW_TOPIC: yes/no | LAST_POSTER: [username]
New posts since cutoff:
- POST_NUMBER | USERNAME | CREATED_AT | SNIPPET (first 200 chars, HTML tags stripped)

After all topics:
TOPICS_WITH_ACTIVITY: [count]
NEW_TOPICS: [count of topics where created_at is also after the cutoff]

If no topics have new activity, return:
TOPICS_WITH_ACTIVITY: 0
```

### Step 3: Triage

After all subagents return, categorize every item into one of three tiers.

**Immediate Action** — The user is directly asked to do something or a deadline is at risk:
- Email classified as IMMEDIATE by the email subagent
- Slack DMs or @mentions where someone is asking the user to do something (look for question marks, "can you", "please", "need you to", action verbs directed at the user)
- Escalation notifications from escalation-related channels
- Messages flagging blocked work or urgent issues ("asap", "blocker", "broken", "impacting")
- New Jira issues with the configured escalation label (flagged as ESCALATIONS by the Jira subagent)

**Needs Response** — The user's input is needed but not time-critical today:
- Email classified as RESPONSE_NEEDED by the email subagent
- Slack questions directed at the user or the team broadly (but not urgent)
- Calendar proposals for future dates
- Requests for votes, reviews, or opinions
- Messages from manager/org channels that reference the user's team or need follow-up
- New Jira issues with Critical or Blocker priority (flagged as HIGH_PRIORITY by the Jira subagent)

**FYI** — Informational, no action needed:
- Email classified as FYI by the email subagent
- Team channel discussions not directed at the user
- Automated reports, dashboards, pipeline results (even if humans replied)
- Org announcements
- Social/watercooler messages
- All other new Jira backlog items (these appear in the New Backlog Items table and do not need to be repeated in FYI)

### Step 4: Deduplicate cross-source items

Look for items that appear across email, Slack, and Jira about the same topic. Merge them into a single entry. Match on:
- Jira issue keys (e.g., AAP-71795 appearing in an email subject, a Slack message, and the backlog table)
- Calendar event titles (e.g., "CVE Severity" declined in email and discussed in Slack)
- Same person + same topic within the same time window

When merging, keep the higher urgency tier and note both sources in the output. Jira issues that appear in both the backlog table and in email/Slack triage items should keep their triage entry and remain in the backlog table (the table is a complete inventory; triage items call out what needs attention).

### Step 5: Generate dashboard

Create parent directories for the output paths if they don't exist.

Write the dashboard to `<output.dashboard_path>` from config, overwriting any existing content.

Use this format:

```markdown
# Daily Brief — [TODAY'S DATE]

**Generated:** [CURRENT TIME] <timezone_abbrev>
**Sources:** Calendar ([N] meetings), Gmail ([X] unread), Slack ([Y] messages across [Z] channels), Jira ([J] new issues), Demos ([D] from team), Forum ([F] posts with activity)
**Scanning since:** [PREVIOUS_BUSINESS_DAY_DATE] 5:00 PM <timezone> *(demos since: [DEMOS_LOOKBACK_DATE])*

> [!summary]
> [TL;DR — 1-2 sentence summary of the day's brief: overall volume/mood, top action items, anything notable]

---

## 📅 Today's Schedule

| Time | Meeting |
|------|---------|
| 9:00 – 9:30 AM | Standup *(recurring)* |
| 10:00 – 11:00 AM | Controller Bug Triage *(recurring, tentative)* |
| 1:00 – 1:30 PM | 1:1 with Jeff Headley |

> ⚠️ Back-to-back: Meeting A → Meeting B (no gap)

---

## 🎬 Team Demos ([count] since last brief)

- **[Author]** — [Summary of demo content]. [link if available] *(posted [date h:MM AM/PM <timezone_abbrev>])*

---

## 🗣 Community Forum ([count] posts with new activity)

- **[Post Title](<forum_base_url>/t/slug/id)** — [N] new replies. [summary of new post content]. [V] total views. Last post by [username]. *(last active: [date])*

---

## 📋 New Backlog Items ([count] since [PREVIOUS_BUSINESS_DAY_DATE])

| Key | Type | Priority | Summary | Reporter |
|-----|------|----------|---------|----------|
| [AAP-12345](<Jira instance URL>/browse/AAP-12345) | Bug | Critical | Gateway auth fails on... | John Westcott |
| [AAP-12346](<Jira instance URL>/browse/AAP-12346) | Story | Normal | Add pagination to... | Amanda Dwyer |

---

## 🔴 Immediate Action

- **[Subject/Topic]** — Context and what's needed. *(source: [email/slack #channel-name])*

## 🟡 Needs Response

- **[Subject/Topic]** — Context and what's needed. *(source: [email/slack #channel-name])*

## 🔵 FYI

### 📧 Email
- **[Subject]** — From [sender]. *(category: [mailing list/notification/calendar])*

### 💬 Team Channels
- **#channel-name** — Summary of key discussions

### 📢 Manager/Org Channels
- **#channel-name** — Summary of key items
```

Rules for the dashboard:
- The TL;DR summary sits between the metadata block and the first `---` separator, wrapped in an Obsidian `> [!summary]` callout block. It should be 1-2 sentences capturing the overall tone of the day (quiet, busy, heavy escalations, etc.), the top action items if any, and anything notably unusual. Write it in a direct, no-filler voice.
- The New Backlog Items section uses a markdown table with Key, Type, Priority, Summary, and Reporter columns.
  - Issue keys must be hyperlinked to `<Jira instance URL>/browse/ISSUE-KEY` (use the Jira instance URL from the user's mcp-atlassian configuration).
  - Issues that were promoted to Immediate Action or Needs Response via triage rules should still appear in the table but be marked with a suffix: ` ⚠️` after the priority for escalation-labeled issues, ` 🔺` for Critical/Blocker priority.
  - If no new issues were created, show "No new backlog items."
  - Sort by priority (Critical/Blocker first), then by created date descending.
- The Today's Schedule section uses a markdown table with Time and Meeting columns.
  - Format time as `h:MM – h:MM AM/PM` (e.g., `9:00 – 9:30 AM`).
  - Append *(recurring)* if the event is recurring.
  - Append *(tentative)* if the user's response status is tentative or needsAction.
  - If there are scheduling notes (back-to-back or conflicts), add them as a blockquote warning below the table.
  - If there are no meetings, show "No meetings today."
- The Community Forum section lists forum posts with new activity since the previous business day cutoff.
  - Each entry shows the post title (hyperlinked to the forum URL), a count of new replies, a brief summary of new post content, total views, the last poster's username, and the last activity date.
  - If a topic is brand new (created after the cutoff), note it as "New post" rather than showing reply count.
  - If there are no posts with new activity, show "No new forum activity."
  - The count in the heading reflects the number of topics with new activity, not total posts on the tag.
- The Team Demos section lists demos posted by team members to the demos channel since the last brief run.
  - Each entry shows the author's name, a 1-2 sentence summary of the demo content, any links (video, recording, PR), and the post timestamp.
  - If there are no demos, show "No new team demos since last brief."
  - The count in the heading reflects the number of demo messages found.
  - Demos are NOT duplicated in the FYI Team Channels section — the demos channel activity is fully handled by this section.
- If a tier has no items, include the heading with "Nothing requiring immediate action." / "No items needing response." / "No new activity."
- In the FYI section, only list channels that had activity. Skip channels with nothing to report.
- Each item should be 1-2 sentences. Enough context to decide whether to dig in, not a full summary.
- Jira issue keys (e.g., AAP-71795, ANSTRAT-1892) must be hyperlinked to `<Jira instance URL>/browse/ISSUE-KEY` (use the Jira instance URL from the user's mcp-atlassian configuration). For example: `[AAP-71795](<Jira instance URL>/browse/AAP-71795)`.
- Slack channel names in the FYI section headings must be hyperlinked to `<Slack workspace URL>/archives/CHANNEL_ID` (use the Slack workspace URL from the user's Slack MCP configuration). For example: `[#aap-gateway](<Slack workspace URL>/archives/C02F01HBCBZ)`. Use the channel IDs from the config.
- Source citations must be specific enough to find the original message:
  - DMs: *(source: DM from [person name])*
  - Channel messages: *(source: slack #channel-name)*
  - Mentions: *(source: [person name] in #channel-name)*
  - Cross-source: *(source: email + DM from [person name])* or *(source: DM from [person] + #channel-name)*
  - Never use generic "slack DMs" — always name the person

After writing the dashboard file, write the state file for the next run:
- Write `<output.state_path>` from config with this content:
  ```json
  {
    "last_run_unix": [CURRENT_UNIX_TIMESTAMP],
    "last_run_iso": "[CURRENT_ISO_8601_TIMESTAMP]"
  }
  ```
- Use the current time at the moment of dashboard generation
- This file is read by Step 1 on the next run to determine the demos lookback window

### Step 6: Present to the user

After writing the dashboard file, display the contents to the user directly in the conversation so the briefing is immediately visible without needing to open a file.

## Error Handling

| Error | Action |
|-------|--------|
| Calendar subagent fails | Note in dashboard header: "Calendar scan failed — check Google Workspace MCP." Omit the Today's Schedule section. |
| Gmail subagent fails | Note in dashboard header: "Gmail scan failed — check Google Workspace MCP." Generate Slack-only dashboard. |
| Any Slack subagent fails | Note in dashboard header which Slack scan failed (DMs, team channels, or org channels). Omit that section; generate dashboard with remaining data. |
| No unread email | Show "No unread email" under the Email section. Continue with Slack data. |
| No Slack activity | Show "No new Slack activity" in the relevant section. Continue with email data. |
| Individual channel not found | Skip that channel. Note in dashboard: "#channel-name — channel unavailable". |
| Jira subagent fails | Note in dashboard header: "Jira scan failed — check mcp-atlassian MCP." Omit the New Backlog Items section. |
| Demos subagent fails | Note in dashboard header: "Demos scan failed — check Slack MCP." Omit the Team Demos section. |
| Community forum fetch fails | Note in dashboard header: "Forum scan failed — check network connectivity." Omit the Community Forum section. |
| State file unreadable | Use 24-hour fallback for demos lookback. Note in dashboard: "*(demos lookback: 24h fallback)*". |
| All data-gathering subagents fail | Write error dashboard: "Daily brief generation failed. All data source scans failed. Run /mcp-check to verify MCP server connectivity." |

## Cron Setup

To run the daily brief automatically on weekday mornings, set up a Claude Code cron:

```
/loop weekdays 8:30am /daily-brief
```

This requires Claude Code to be running. If it is not running at the scheduled time, the cron will not fire.
