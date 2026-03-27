---
source_type: gdrive
source_id: "17L9r6ZSy6VbKNcTw0haQRrWXBkNnSdb9"
source_name: "User-Stories-Applied-Mike-Cohn.pdf"
last_summarized: 2026-03-03
---

# User Stories Applied (Mike Cohn) -- AI Product Owner Coaching Reference

A coaching-optimized summary of "User Stories Applied: For Agile Software Development" (Addison-Wesley, 2004). Organized by coaching use case, not chapter order. All content derived from the source text.

---

## 1. What User Stories Are: The Three Cs

Ron Jeffries named the three aspects of a user story Card, Conversation, and Confirmation.

| Component | Role | Key Insight |
|-----------|------|-------------|
| **Card** | Short written description used for planning and as a reminder | Rachel Davies: cards "represent customer requirements rather than document them" |
| **Conversation** | Discussions that flesh out details between developers, customer, and users | Where the real requirements live; the card is just a reminder to have this talk |
| **Confirmation** | Acceptance tests that document details and verify the story is complete | Written on the back of the card; specify expectations so developers know when they are done |

A story describes functionality valuable to either a user or purchaser of the system. Stories are not contracts -- they are promises to converse later.

### What Stories Are NOT

| Not This | Why |
|----------|-----|
| IEEE 830 requirements ("The system shall...") | Tedious, error-prone, boring to read; focus on checklists rather than user goals |
| Use cases | Use cases are more formal, broader in scope (one use case may cover many stories), and require readers to learn formatting conventions |
| Interaction design scenarios | Scenarios walk through specific instances; stories are less detailed and more planning-oriented |

**Key distinction**: IEEE 830 lists describe attributes of a product; stories describe a user's goals. Cohn illustrates this with a lawn mower example -- requirements like "gasoline engine, four wheels, rubber tires, steering wheel" sound like a car, but the user's actual goals ("make it easy to mow my lawn," "I am comfortable while using the product") reveal the need for a riding lawn mower.

---

## 2. Writing Good Stories

### Format

Cohn uses simple, direct sentences for most examples:

- "A user can search for jobs."
- "A company can post new job openings."
- "A user can limit who can see her resume."

The Connextra template is also referenced:

```
I as a (role) want (function) so that (business value)
```

### Guidelines for Good Stories

| Guideline | Explanation |
|-----------|-------------|
| **Start with goal stories** | Consider what each user role wants to achieve with the system |
| **Slice the cake** | Each story should cut through all layers of the application (UI, logic, data) |
| **Write closed stories** | A story should end with a user achieving a meaningful goal, like finishing a task and taking a coffee break |
| **Put constraints on cards** | Mark non-functional requirements as "Constraint" -- they influence other stories but are not directly estimated |
| **Size to the horizon** | Near-term stories are small and detailed; distant stories can be large epics |
| **Keep the UI out** | Avoid user interface specifics for as long as possible |
| **Include user roles** | Write "A Job Seeker can post a resume" not "A user can post a resume" |
| **Write for one user** | "A Job Seeker can remove her own resumes" is clearer than "Job Seekers can remove resumes" |
| **Write in active voice** | "A Job Seeker can post a resume" not "A resume can be posted by a Job Seeker" |
| **Customer writes** | Responsibility for writing stories resides with the customer; developers help but do not own |
| **Don't number cards** | Numbering adds pointless overhead; use a short title instead |
| **Don't forget the purpose** | The card is a reminder to discuss the feature -- keep it brief |

### Common Mistakes

| Mistake | Example | Better |
|---------|---------|--------|
| Too technical (no user value) | "The program will connect to the database through a connection pool" | "Up to fifty users should be able to use the application with a five-user database license" |
| Specifying implementation | "The software will be written in C++" | Only valid if the user of the system (e.g., a programmer using an API) would actually care |
| Too much detail on card | Card with credit card processing details, expiration date fields, storage rules | Card with story + notes about open questions; details become tests on the back |
| UI details too early | "Print dialog allows the user to edit the printer list. The user can add or remove printers..." | Focus on goals; defer UI decisions |
| Not valuable to users/buyers | "All connections to the database are through a connection pool" | "Up to fifty users should be able to use the application with a five-user database license" |

---

## 3. The INVEST Criteria

Bill Wake's acronym for six attributes of a good story:

| Criterion | Meaning | How to Fix Violations |
|-----------|---------|----------------------|
| **Independent** | Avoid dependencies between stories; dependencies create prioritization and estimation problems | Combine dependent stories into one, or find a different splitting dimension |
| **Negotiable** | Cards are reminders to converse, not contracts; details are worked out in conversation | If a card feels like a specification, strip detail and move it to tests |
| **Valuable** | Every story must be valued by users or purchasers (not just developers) | Rewrite technical stories to expose the benefit: "All errors are presented to the user and logged in a consistent manner" |
| **Estimable** | Developers must be able to estimate the story | Three causes of failure: lack of domain knowledge (discuss with customer), lack of technical knowledge (run a spike), story too big (split it) |
| **Small** | Stories must fit within an iteration; epics are too large to plan with | Split compound stories or complex stories (see splitting section) |
| **Testable** | Must be verifiable through tests | "A user must find the software easy to use" is not testable; "New screens appear within two seconds in 95% of all cases" is testable |

### Dependency Example from Cohn

Three stories for credit card payment (Visa, MasterCard, Amex) are interdependent -- the first card type takes 3 days, the others 1 day each, but you don't know which is "first." Solutions:
- **Combine**: "A company can pay for a job posting with a credit card" (5 days total)
- **Re-split**: "A customer can pay with one type of credit card" + "A customer can pay with two additional types"

---

## 4. Gathering Stories

Cohn uses the Robertson and Robertson term **trawling** -- requirements are not sitting there waiting to be "captured" or "elicited." Different-sized nets catch different-sized requirements, and requirements mature, change, and die over time.

### Techniques

| Technique | Best For | Key Guidance |
|-----------|----------|--------------|
| **User interviews** | Primary technique for discovering stories | Ask open-ended, context-free questions; avoid "Would you like X?" (closed-ended); instead ask "What would you be willing to give up to get X?" |
| **Questionnaires** | Confirming priorities across a large user base | Not recommended as a primary technique; cannot follow interesting paths |
| **Observation** | Discovering real needs vs. stated needs | Users' workarounds reveal true requirements; example: nurses asked for a text field but really needed the system to log decisions automatically |
| **Story-writing workshops** | Most effective way to rapidly trawl for stories | Combine brainstorming with low-fidelity prototyping; walk through user workflows |

### Story-Writing Workshop Process

1. Decide which user role or persona to start with
2. Draw an empty box representing the main screen; ask what the role can do from there
3. For each action, draw a line to a new box, label it, write a story
4. Take a depth-first approach through the workflow
5. Repeat for each user role
6. Output: a set of stories covering the major workflows, without any UI design commitment

### Interview Anti-Pattern

Cohn's example of a bad survey question: "Would you like our new application in a browser?" This is closed-ended and fails to mention tradeoffs. Better: "What would you be willing to give up in order to have our next generation product run within a browser?"

---

## 5. User Roles and Personas

### Why User Roles Matter

Writing all stories from the perspective of a generic "user" leads teams to miss stories for users who do not fit the primary user type.

### Role Modeling Steps

1. **Brainstorm** roles on index cards (everyone writes simultaneously, no discussion)
2. **Organize** by arranging cards -- overlapping roles near each other, distinct roles apart
3. **Consolidate** similar roles into a manageable set
4. **Refine** each role with defining attributes

### Role Attributes

Define roles along these dimensions:
- Frequency of use (daily vs. occasional)
- Domain expertise level
- Technical proficiency level
- General computer proficiency
- Goals for using the system

### Personas

Personas are imaginary representations of user roles -- fictional but realistic:

- Give the persona a name and narrative description
- Make them specific enough to guide design decisions
- Use personas to resolve disagreements: "What would this persona need?"

### Extreme Characters

Cohn describes a technique of using extreme characters (e.g., a parole officer, a drug dealer) during brainstorming to surface stories that realistic personas might miss. Use only for brainstorming, not as actual target users.

---

## 6. Acceptance Testing and Acceptance Criteria

### Core Principles

- **Write tests before coding** -- this communicates expectations early and saves developer time
- **The customer specifies the tests** -- possibly with help from a dedicated tester
- **Testing is part of the process** -- not a phase that happens after development

### How to Write Acceptance Tests

Tests go on the back of the story card as short reminders. From Cohn's credit card story example:

```
- Test with Visa, MasterCard and American Express (pass).
- Test with Diner's Club (fail).
- Test with a Visa debit card (pass).
- Test with good, bad and missing card ID numbers from the back of the card.
- Test with expired cards.
- Test with different purchase amounts (including one over the card's limit).
```

These tests captured that the system handles three card types and rejects others. Noting "expired cards" as a test before coding reminds the programmer of a situation she might have forgotten.

### How Many Tests?

Tests can be added or removed at any time. They are short and incomplete by design. The goal is to convey expectations and define when a story is done.

### Types of Testing

Beyond functional story testing, consider: user interface testing, usability testing, performance testing, and stress testing.

### Example: Search Story Acceptance Tests

Story: "A user can do a basic simple search that searches for a word or phrase in both the author and title fields."

Tests:
- Search for a word known to be part of a title but unlikely to be an author (e.g., "navigation")
- Search for a word likely to be an author but unlikely to be a title (e.g., "John")
- Search for a word unlikely to be in either (e.g., "wookie")

---

## 7. Estimating and Planning with Stories

### Story Points

- A relative measure of story size -- each team defines them as they see fit
- Can represent ideal days, complexity, or "Nebulous Units of Time" (NUTs, per Joshua Kerievsky)
- A 4-point story is expected to take roughly twice as long as a 2-point story
- Teams should constrain estimates to pre-defined values: 1/2, 1, 2, 3, 5, 8, 13, 20, 40, 80

### Estimation Process (Wideband Delphi Variant)

1. Customer reads a story to the developers; developers ask clarifying questions
2. Each developer writes an estimate privately on an index card
3. All cards revealed simultaneously
4. High and low estimators explain their reasoning
5. Repeat until convergence (rarely more than 3 rounds)
6. Customer participates to answer questions but does NOT estimate

### Triangulation

After the first few estimates, compare new estimates against existing ones. Pin story cards to a wall in columns by story point value. Each new estimate should be "about the same" as others in its column.

### Velocity

- **Velocity** = story points completed per iteration (only count fully finished stories)
- Use measured velocity from the prior iteration to plan the next
- Do NOT retroactively change story point values after completion
- Do NOT compare velocity across teams (story points are team-specific)

### Release Planning

1. Select an iteration length (1-4 weeks, consistent throughout the project)
2. Customer prioritizes stories using MoSCoW: Must Have, Should Have, Could Have, Won't Have
3. Developers estimate velocity
4. Allocate stories to iterations so that points per iteration do not exceed velocity
5. Re-plan at the start of each iteration based on actual velocity

### Iteration Planning

1. Customer and developers discuss the stories selected for the iteration
2. Stories are disaggregated into developer tasks
3. Individual developers accept responsibility for tasks
4. Task estimates are in ideal hours, owned by individuals (unlike story estimates, which are owned by the team)

### Burndown Charts

- **Iteration burndown chart**: shows story points remaining at end of each iteration; reflects both progress and scope changes
- **Daily burndown chart**: shows hours remaining each day within an iteration; updated by developers on a whiteboard
- Track hours remaining, not hours expended

---

## 8. Splitting Large Stories

### Two Types of Epics

| Type | Description | Splitting Strategy |
|------|-------------|-------------------|
| **Compound story** | An epic that comprises multiple shorter stories | Disaggregate by workflow, data boundaries, or CRUD operations |
| **Complex story** | Inherently large, cannot easily be disaggregated | Split into a timeboxed spike (research) + implementation story |

### Splitting Patterns (from the Book)

| Pattern | Example |
|---------|---------|
| **By CRUD operations** | "A user can post her resume" splits into: create, edit, delete, activate/deactivate, multiple resumes |
| **By data boundaries** | Resume splits into: education, job history, salary history, publications, presentations, community service, objective |
| **Spike + implementation** | "Investigate credit card processing" (timeboxed) + "A user can pay with a credit card" |
| **By search type** | "A user can search for books" splits into: basic search (author + title) + advanced search (any combination of fields) |
| **By priority within a feature** | "Edit account info" splits into: edit credit card (high priority) + edit addresses (can wait) |

### When Splitting Goes Wrong

- Stories that are too small: "A Job Seeker can enter a date for each community service entry on a resume" -- roll these up
- Splitting too frequently during iteration planning indicates stories should be pre-split during backlog refinement
- Tip from Cohn: when possible, put the spike in one iteration and the implementation stories in subsequent iterations

### Combining Small Stories

Tiny stories (bug fixes, minor UI changes) should be combined into a single story representing a half-day to several days of work. Staple the cards together with a cover card.

---

## 9. Story Smells (Anti-Patterns Catalog)

Cohn's "catalog of bad smells" -- indicators that something is amiss:

| Smell | Symptom | Solution |
|-------|---------|----------|
| **Stories too small** | Frequent need to revise estimates; overlapping work between stories | Combine for planning purposes; split only when slotted into an iteration |
| **Interdependent stories** | Difficulty planning iterations due to dependencies | Combine the dependent stories or find a different split dimension |
| **Goldplating** | Developers adding features not planned for the iteration | Increase visibility: daily standups, end-of-iteration demos, QA involvement |
| **Too many details** | More time writing about stories than talking about them | Tom Poppendieck: "If you run out of room, use a smaller card" |
| **UI detail too soon** | Stories written early include UI specifics | "When viewing details about a job, a Job Seeker may view information about the hiring company" -- no mention of specific pages |
| **Thinking too far ahead** | Stories hard to fit on cards; proposals for story templates or finer-grained estimates | Remind the team: it is impossible to identify all requirements in advance |
| **Splitting too many stories** | Frequently splitting stories during iteration planning | Take a pass through remaining stories and pre-split proactively |
| **Customer has trouble prioritizing** | Stories too large or value not clear | Split large stories so customer can select pieces; rewrite stories to expose business value |
| **Customer won't write/prioritize** | Customer avoids responsibility | Find a non-threatening way for the customer to express opinions; offer to take responsibility for final decisions |

### Goldplating Example

A developer was given a story to convert a crowded screen to a tabbed dialog. After finishing, he also added the ability to tear tabs from the dialog and move them around the screen -- functionality the customer never asked for.

---

## 10. Good vs. Bad Stories (Examples from the Book)

### Stories That Are NOT Good (from Chapter 1 exercises)

| Bad Story | Why It Fails |
|-----------|--------------|
| "The software will be written in C++" | Users of BigMoneyJobs don't care about programming language |
| "The program will connect to the database through a connection pool" | Users don't care about technical implementation |
| "All graphing and charting will be done using a third-party library" | No value to users or purchasers |
| "The software will be released by June 30" | Not a description of functionality |
| "The system will use Log4J to log all error messages to a file" | Technical implementation; rewrite as user-facing value |

### Stories That ARE Good

| Good Story | Why It Works |
|------------|--------------|
| "A user can search for jobs" | Clear user goal, valuable, estimable |
| "A user can limit who can see her resume" | Specific user need, testable |
| "A user can undo up to fifty commands" | Clear, testable, user-valued |
| "A user can export data to XML" | Better than "A user can select an 'Export to XML' feature" (which specifies UI) |
| "All runtime errors are logged in a consistent manner" | Valuable to users even though technical-sounding |

### Non-Functional Requirements as Constraints

Constraints are marked as such and are not directly estimated:

| Constraint | Why It Works |
|------------|--------------|
| "A repeat customer must be able to find one book and complete an order in less than 90 seconds" | Measurable performance requirement |
| "The system must support peak usage of up to 50 concurrent users" | Testable capacity requirement |
| "Orders made on the website have to end up in the same order database as telephone orders" | Integration constraint |

### The BigMoneyJobs/Sailing Bookstore Full Example

Cohn walks through a complete example of a sailing bookstore with user roles (Experienced Sailor "Teresa," sailing school operator "Captain Ron," Novice Sailor, Non-Sailing Gift Buyer, Report Viewer, Administrator), 27 stories, estimation sessions, a release plan with two two-week iterations, and acceptance tests for each story. The estimation session demonstrates the full Wideband Delphi process, including story splitting during estimation when developers discover compound or unclear stories.

---

## Quick Reference: Coaching Checklist

Use during backlog refinement or story writing sessions:

- Is this story written from a user's or buyer's perspective?
- Does it use a specific user role (not generic "user")?
- Is the goal stated without specifying UI or implementation?
- Does it pass all six INVEST criteria?
- Are acceptance tests written on the back of the card?
- Is the story small enough for one iteration?
- Has the team had (or scheduled) a conversation about this story?
- Can a tester write test cases from the acceptance criteria?
- Does the story deliver a vertical slice through all application layers?
- Is the story written in active voice for a single user?

---

## Key Terminology

| Term | Cohn's Definition |
|------|-------------------|
| **Epic** | A story too large to be worked in one iteration; can be compound or complex |
| **Theme** | Main areas of focus for a release (Kent Beck's term) |
| **Spike** | A timeboxed experiment to learn about an area of the application; reduces uncertainty |
| **Velocity** | The number of story points a team completes per iteration |
| **Story Points** | Relative estimates of size/complexity/effort; team-specific, not comparable across teams |
| **Constraint** | A story marked as "Constraint" that must be obeyed rather than directly implemented |
| **Trawling** | Robertson and Robertson's metaphor for gathering requirements -- like fishing with different mesh sizes |
| **Customer Team** | Those who ensure software meets user needs: may include testers, product manager, real users, interaction designers |
| **MoSCoW** | Prioritization from DSDM: Must have, Should have, Could have, Won't have this time |
| **INVEST** | Bill Wake's acronym: Independent, Negotiable, Valuable, Estimable, Small, Testable |
| **Three Cs** | Ron Jeffries' Card, Conversation, Confirmation |
| **Triangulation** | Verifying an estimate by comparing it to other estimated stories |

---
