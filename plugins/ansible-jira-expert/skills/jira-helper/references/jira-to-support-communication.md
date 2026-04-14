---
source_type: gdrive
source_id: "13RSiaImzBYvejD9wBYGRj05fNiqdWROb7tSvaM9yThI"
source_name: "Ansible: Use Jira to support communication"
last_summarized: 2026-04-01
---

# Ansible: Use Jira to Support Communication - Summary

This document addresses common questions related to Collaborative Delivery, specifically: "What do I do if something unexpected is going on and/or I have concerns?" This approach is recommended for Features, but is applicable to all issue types in Jira.

## Visibility Approach Overview

Four escalation options with increasing visibility and implied urgency/severity:

| Visibility Level | Approach | Description |
|-----------------|----------|-------------|
| **Least visible** | Comment + @mention individuals | Direct notification to specific people |
| ↓ | Discussion Needed field | Flags for scheduled team discussions |
| ↓ | Blocked / Blocked Reason fields | Makes problems visible across dashboards |
| **Most visible** | Combined approach (Blocked, Discussion Needed, Need Info From, Comments) | Uses multiple fields for maximum visibility |

**Note:** Urgency/severity refers to the conceptual level of urgency, not specific Jira fields.

## Jira Notification System

**All Ansible projects** use custom notification scheme (RH1-NS-001):

- Everyone in named Contributor fields receives email notifications
- Watchers are also notified via email
- Ensures broad visibility for important communications

## Option 1: Comment with @Mentions

**When to Use:**

- Noticed something odd about the Jira issue and want to raise awareness
- Need to inform people about something that might impact expectations/delivery
- Have a question about the issue status or requesting an update

**How to Use:**

1. Navigate to the relevant issue
2. Add a comment using the @ symbol to mention specific individuals
3. The mentioned individuals will receive email notifications with your comment and issue link
4. For ANSTRAT issues: all named Contributors and watchers are automatically notified

## Option 2: Discussion Needed Field

**When to Use:**

- Option 1 didn't get a response or nothing happened
- Work isn't completely blocked but has staffing issues needing visibility
- Situation requires group discussion at a scheduled call

**How to Use:**

1. Navigate to the issue
2. Click Edit button
3. Go to "Escalation" tab and find Discussion Needed field (multi-select)
4. **Always add a comment** describing the situation and what's needed

### Discussion Needed Field Values

| Value | Purpose | Usage |
|-------|---------|-------|
| **Feature Refinement** | Features/Initiatives for Ansible Feature Refinement call | Populates 'Discussion Needed' view in Unified Backlog |
| **PM Team call** | PM coordination on outcomes, features, initiatives | For re-prioritization, learning, coordination discussions |
| **Priorities Alignment** | Strategy/leadership level discussions | Weekly leadership priorities alignment call |
| **Scrum of Scrums** | Epic, Story, Task, Spike, Bug discussions | Shows in Ansible Scrum of Scrums dashboard gadget |
| **Team Discussion** | Surface issues for team calls | Filterable in team board backlogs during sprint ceremonies |
| **Staff Engineering review** | Issues needing Architect support | Reviewed in weekly Staff Engineering call |

## Option 3: Blocked / Blocked Reason Fields

**Purpose:** Make blocking problems visible across the organization

**Broader Visibility:**

- Blocked field is available and filterable on Scrum of Scrums dashboard
- Teams can configure Kanban boards with:
  - Blocked quick filters
  - Blocked swimlanes
  - Blocked color coding

**Reference:** See [Ansible Knowledge Base Wiki](https://spaces.redhat.com/x/DGWuEw) for detailed definitions and scenarios.

## Option 4: Combined Approach

**When to Use:**

- Significant urgency and scrutiny around a particular issue
- Individuals need regular notifications
- Clear action needed to unblock/move forward
- Multiple stakeholders need coordination

**How to Use:**

- Use judgment to combine Options 1-3 based on situation severity
- Available fields to combine: Blocked / Blocked Reason, Discussion Needed, Need Info From, and Comments
- Follow instructions from previous options to set multiple fields
- Ensure comprehensive communication coverage

## Best Practices

1. **Start with least visible option** and escalate as needed
2. **Always provide context** in comments about what decision/action is required
3. **Use appropriate Discussion Needed values** for your specific situation
4. **Reach out for help** via #ansible-jira-support Slack channel
5. **Consider your audience** when selecting visibility level

## Key Links

- [Knowledge Base Wiki](https://spaces.redhat.com/x/zYLGFw)
- [Collaborative Delivery Presentation](https://docs.google.com/presentation/d/1r8tgHoTdy0TIgHh44rioWLqRDrETVXdekawsVyjuePc/edit#slide=id.g2600e58d299_0_0)
- [Ansible Knowledge Base Wiki](https://spaces.redhat.com/x/DGWuEw)
- [#ansible-jira-support](https://redhat-internal.slack.com/archives/C01GWN5J2KS) Slack channel
