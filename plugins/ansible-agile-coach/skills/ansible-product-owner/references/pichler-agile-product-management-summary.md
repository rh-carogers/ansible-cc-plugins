# Pichler: Agile Product Management with Scrum -- Coaching Reference

Source: Roman Pichler, *Agile Product Management with Scrum: Creating Products that Customers Love* (Addison-Wesley, 2010). Google Drive file ID: `1LSdQ2VpNj_uZB1ylEiUGVbRVEyvIRwRH`

---

## 1. The Product Owner Role

The Product Owner is **one person** responsible for managing the Product Backlog and ensuring the value of the work the team performs. The role unites authority and responsibility traditionally scattered across product manager, project manager, and customer/sponsor roles.

### Desirable Characteristics

| Trait | Description |
|---|---|
| Visionary and Doer | Envisions the product AND sees it through to completion |
| Leader and Team Player | Provides direction yet acts as *primus inter pares* (first among peers) |
| Communicator and Negotiator | Bridges "the suits" and "the techies"; says no when needed |
| Empowered and Committed | Has decision-making authority and management sponsorship |
| Available and Qualified | Full-time role; domain expertise, UX passion, budget management |

### Key Relationships

- **With the Team**: Product Owner is a Scrum team member. Colocation is ideal. One-hour rule: spend at least one hour per day in the team room if not colocated. Minimize team composition changes within and across releases.
- **With the ScrumMaster**: Complementary roles -- PO owns the "what" (right product), SM owns the "how" (right process). One person must never play both roles.
- **With Stakeholders**: Involve customers, users, marketing, sales, and service early and regularly via sprint review meetings and early releases.

### Product Owner Dos and Don'ts (from Lyssa Adkins)

| Do | Don't |
|---|---|
| Say what needs to get done | Say how to do it or how much it will take |
| Challenge the team | Bully the team |
| Build a high-performance team | Focus on short-term deliveries only |
| Practice business-value-driven thinking | Stick to original scope "no matter what" |
| Protect the team from outside noise | Worry the team with changes until they are real |
| Incorporate change between sprints | Allow change to creep into sprints |

---

## 2. Product Vision and Strategy

The product vision is a sketch of the future product -- the overarching goal and reason for being. It should answer:

- Who will buy/use the product? (target customer, target user)
- Which customer needs will it address? What value does it add?
- Which product attributes are critical for success?
- How does it compare to competitors? What are its unique selling points?
- What is the business model and revenue sources?
- Is the product feasible?

### Vision Qualities

- **Shared and Unifying**: Created collaboratively; everyone buys in. A vision is truly shared when people are "committed to one another having it" (Senge).
- **Broad and Engaging**: Guides development but leaves room for creativity. Avoid overspecification.
- **Short and Sweet**: Must pass Moore's elevator test. Blockbuster products have no more than six product attributes. Focus on three to four key factors that would incite someone to buy.

### The Minimal Marketable Product

Envision the product with **minimum functionality** that meets selected customer needs. Benefits of minimal products:

- Faster time to market
- Lower development cost, higher ROI
- Earlier payments improve cash flow
- Accelerated learning from market response
- Better risk mitigation -- less money lost if product underperforms

The vision should cover only the **next product version**. Grand ambitions are best realized one step at a time.

### Customer Needs vs. Product Attributes

- **Customer needs** define which market segment to address (the "why")
- **Product attributes** are critical properties the product must have to meet those needs (the "what")
- Attributes can be functional (features) or nonfunctional (performance, usability, design)
- Prioritize conflicting attributes using: Sacrifice others for this / Try to keep / Sacrifice these for others

### Product Road Map

A planning artifact showing how the product evolves across versions. Guidelines:

- State for each version: projected launch date, target customers and needs, top three to five features
- Create only after the product has been successfully introduced to market
- Cover a realistic horizon (6-12 months), not two to three years
- Road maps are living documents; they evolve and change

---

## 3. Product Backlog Management

The product backlog is a prioritized list of outstanding work. It supersedes traditional requirements specifications.

### DEEP Qualities

| Quality | Meaning |
|---|---|
| **D**etailed Appropriately | High-priority items are fine-grained; low-priority items are coarse-grained |
| **E**stimated | Items sized in story points or ideal days |
| **E**mergent | Contents evolve based on feedback; items are added, modified, removed |
| **P**rioritized | Most important items at the top; implemented first |

### Grooming Process

Grooming is collaborative (Scrum allocates up to 10% of team capacity for it). Four activities:

1. **Discover and describe** new items; modify or remove existing ones
2. **Prioritize** the backlog
3. **Decompose and refine** high-priority items for the next sprint
4. **Size** items

Grooming tools: paper cards are cheap, collaborative, and complement electronic tools.

### Describing Items

- Prefer **user stories** (name, narrative, acceptance criteria). Coarse-grained stories are called **epics**.
- Supplement with: user role summaries, story sequences, business rule diagrams, UI sketches, prototypes
- Structure backlogs using **themes** (e.g., email, calendar, voice). Each theme should contain two to five coarse-grained items initially.

### Prioritization Factors

| Factor | Guidance |
|---|---|
| **Value** | Is the item necessary to bring the product to life? If not, discard it. Always ask: could the product succeed without this item? |
| **Knowledge / Uncertainty / Risk** | Uncertain and risky items should be high-priority to drive out risk early (fail-early approach) |
| **Releasability** | Prioritize to enable early, frequent releases that generate feedback |
| **Dependencies** | Resolve by combining dependent items into one or slicing them differently |

### Sprint Preparation

- **Choose a sprint goal**: Broad but realistic; creates alignment and minimizes variation
- **Prepare just enough items just in time**: Detail only items for the upcoming sprint
- **Decompose progressively**: Break epics into coarse stories, then into fine-grained stories across multiple sprints
- **Ensure clarity, testability, feasibility**: Common understanding, acceptance criteria present, completable in one sprint

### Estimation

- **Story points**: Coarse-grained relative measures. Nonlinear scale: 0, 1, 2, 3, 5, 8, 13, 20
- **Planning Poker**: Team-based consensus estimation using cards. Converge through discussion rounds.
- **Fast-track estimation**: Wall-based grouping when time is short; lower quality but very fast.
- Only team members who create increments should estimate. PO and SM do not estimate.

### Nonfunctional Requirements

- **Global** nonfunctional requirements (e.g., performance): Detail early, incorporate into the Definition of Done
- **Local** nonfunctional requirements: Attach as constraints to specific stories
- Capture UX requirements as sketches, storyboards, and prototypes rather than text

---

## 4. Release Planning and Roadmapping

### Core Principle: Fix Time, Flex Functionality

- Fixing functionality is harmful -- it prevents adaptation based on feedback
- Identify the **window of opportunity** from the product vision
- Fixing date + stable teams makes budget straightforward

### Quality Is Frozen

- Quality criteria are captured in the Definition of Done
- Every sprint must produce a (potentially) shippable increment
- Never accept work that violates done criteria; quality compromises create **technical debt**

### Early and Frequent Releases

- Release to target customers early and frequently to let the product evolve based on real usage
- Each release must have right quality even if features are partial
- Use **quarterly cycles** if the project exceeds three to four months

### Velocity

- Sum of story points for accepted items in a sprint
- Team-specific; cannot be compared across teams unless they share the same estimation semantics
- May take two to three sprints to stabilize on new teams

### Release Burndown

- **Burndown chart**: Plots remaining effort (y-axis) over sprints (x-axis). Extend trend line to forecast completion.
- **Burndown bar**: Differentiates between reestimation and scope changes (top moves = estimates; bottom moves = items added/removed)

### Release Plan

Based on four factors: product backlog items, remaining effort, velocity, and time. Contents per sprint: velocity forecast, actual velocity, dependencies, and release milestones.

**Velocity Forecasting** (multipliers from Cohn):

| Sprints Completed | Low Multiplier | High Multiplier |
|---|---|---|
| 1 | 0.60 | 1.60 |
| 2 | 0.80 | 1.25 |
| 3 | 0.85 | 1.15 |
| 4+ | 0.90 | 1.10 |

After 5+ sprints: use sorted velocity list and 90% confidence intervals (Cohn).

### Large Project Planning

- Establish a **common baseline** for estimates across teams
- **Look-ahead planning**: Prepare items two to three sprints out; identify and resolve inter-team dependencies
- **Pipelining** (last resort): Spread delivery of one item across sprints when teams must supply to each other

---

## 5. Working with Stakeholders and Sprint Meetings

### Sprint Planning

- PO ensures backlog is groomed before the meeting. PO attends to clarify requirements.
- PO defines "what"; team decides "how much" and "how." PO must not dictate workload.
- Commitment is not a guarantee. Sustainable pace is essential.

### Daily Scrum

- PO should attend to understand progress, answer questions, share release-level information
- Do not assign tasks, identify tasks, or comment on individual progress

### Sprint Review

- PO compares increment to sprint goal; accepts or rejects each item against the Definition of Done
- Never accept unfinished or defective items (they earn zero points and return to the backlog)
- Solicit stakeholder feedback: What must change? Is the vision still valid? Is functionality missing or excessive?
- Keep meetings low-key -- no formal presentations or slides
- **Just-in-time reviews**: Provide feedback during the sprint as results emerge, not just at the review

### Sprint Retrospective

- PO participates regularly to contribute improvement measures and strengthen team relationship
- All improvement measures must be actionable, usually implemented in the next sprint
- Large improvements are added to the product backlog

### Large Project Meetings

- **Joint sprint planning**: Teams meet at start and reconvene after individual planning
- **Scrum of Scrums**: Daily coordination meeting among team representatives
- **Joint sprint review**: Science-fair format -- each team sets up a station; reviewers rotate (Primavera model)
- **Joint retrospective**: Use Open Space Technology for self-organized problem-solving

---

## 6. Scaling Product Ownership

### Chief Product Owner

- One person in charge of creating and implementing the product vision across multiple teams
- Guides other POs, ensures consistent communication, optimizes project-wide progress
- Has final say when no consensus can be reached
- One PO can sustainably look after no more than two teams

### Product Owner Hierarchies

- **Simple**: Flat team of POs with a chief PO (e.g., three POs for three teams)
- **Complex**: Multiple layers for large projects (e.g., mobile phone with Entertainment, Communications, Photo/Video sub-POs)

### Team Structure and PO Selection

- **Feature teams** (preferred): Work on cohesive requirements; PO is typically a product manager
- **Component teams**: Work on subsystems; PO is typically an architect or senior developer
- Use feature teams whenever possible; component teams only when necessary

### Scaling the Product Backlog

- Use **one product backlog** for the entire product -- avoid team- or component-specific backlogs
- Extend the **grooming horizon** to two to three sprints ahead
- Provide **separate backlog views** per team to prevent conflicts

---

## 7. Common Pitfalls and Anti-Patterns

### Product Owner Anti-Patterns

| Anti-Pattern | Symptoms | Remedy |
|---|---|---|
| **Underpowered PO** | Must consult boss for every decision; erodes team confidence | Ensure full empowerment and sponsorship from the right level |
| **Overworked PO** | Neglects grooming, misses meetings, slow to answer | Free from all other responsibilities; ensure team supports PO (10% capacity) |
| **Partial PO** | Role split between product manager and backlog writer | Unite strategic and tactical aspects in one person |
| **Distant PO** | Works separately from team; mistrust and miscommunication | Colocate; one-hour rule minimum |
| **Proxy PO** | Placeholder without real authority | Address root cause (overwork, distance), not the symptom |
| **PO Committee** | Group without one person in charge; "death by committee" | Always appoint a chief product owner |
| **Bungee PO** | Appears at planning, vanishes, reappears at review | PO responsibilities must be number-one priority |
| **Passive PO** | Acts as bystander at sprint review | Actively accept/reject items, provide constructive feedback |

### Vision Anti-Patterns

| Anti-Pattern | Description |
|---|---|
| No Vision | Feature soup -- features incorporated without connection |
| Prophecy Vision | Treating the vision as guaranteed future; failing to inspect and adapt |
| Analysis Paralysis | Overdoing market research without making progress |
| "We Know Best" | Ignoring customers; relying solely on internal intuition |
| Big Is Beautiful | Overly ambitious big-bang development; high risk of failure |

### Backlog Anti-Patterns

| Anti-Pattern | Description |
|---|---|
| Disguised Requirements Spec | Too detailed, too comprehensive; freezes decisions early |
| Wish List for Santa | Contains everything ever imagined; impossible to prioritize |
| Requirements Push | PO writes items alone and hands off to team |
| Grooming Neglect | Poorly groomed backlog leads to bad sprint planning |
| Competing Backlogs | Team works on multiple backlogs per sprint; nothing progresses |

### Release Planning Anti-Patterns

| Anti-Pattern | Description |
|---|---|
| No Release Burndown/Plan | No tracking; difficult to assess progress |
| PO in the Passenger Seat | PO delegates planning to SM or team instead of driving it |
| Big-Bang Release | All functionality shipped at once; no feedback incorporation |
| Quality Compromises | Cutting corners creates technical debt and unsustainable pace |

---

## 8. Key Frameworks and Tools

### Kano Model

Classifies product functions into three types to guide feature selection:

| Type | Description | Example (mobile phone) |
|---|---|---|
| **Basics** | Must-have; absence renders product useless; satisfaction stagnates quickly | Making/receiving calls, text messages |
| **Performance** | "The more, the better"; linear increase in satisfaction; not sufficient to differentiate | Lighter weight, faster startup |
| **Delighters** | Excite customers; may address latent needs; provide competitive advantage | Attractive design, personalization |

Key prediction: Over time, delighters become performance functions, and performance functions become basics.

Apply to both the product vision (performance + delighters) and the product backlog (basics).

### Vision Box

Mock-up of the product's shipping package. Front: product name, graphical representation, three selling-point bullets. Back: additional details. Quick exercise to test if a shared vision exists.

### Trade Journal Review

Team members write the review they would want to read about the product at launch. Tests for a commonly understood and shared vision.

### Personas and Scenarios

- **Personas**: Hypothetical archetypes representing target customers/users (with names and relevant context)
- **Scenarios**: Describe how personas achieve goals without and with the product
- **Consumption maps**: Map activities before and after the product to establish the value proposition

### Prototypes and Spikes

- Throwaway artifacts for rapid knowledge creation (paper prototypes, sketches, executable spikes)
- Follow the Deming cycle: Plan (hypothesis), Do (validate), Check (review), Act (adapt)

### Planning Poker

Consensus-based team estimation. Each member plays a card with their estimate; outliers explain reasoning; iterate until convergence. Uses nonlinear story point scale (0, 1, 2, 3, 5, 8, 13, 20).

### Release Burndown Chart and Bar

- **Chart**: Simple two-axis plot (effort vs. sprints) with trend line for forecasting
- **Bar**: Adds granularity -- distinguishes reestimation from scope changes

### Definition of Done

Shared criteria every product increment must fulfill (typically: implemented, tested, documented). Created before the first sprint by PO, SM, and team. Kept visible throughout the project. Nonfunctional requirements should be incorporated.

### Product Backlog Structure

Themes > Epics > User Stories, with effort estimates. Nonfunctional requirements tracked separately and incorporated into the Definition of Done.

---

## 9. Transitioning Into the Product Owner Role

### For New Product Owners

1. **Know yourself**: Assess skills against PO responsibilities; identify gaps
2. **Develop and grow**: Attend PO training; embrace Scrum values (commitment, focus, openness, respect, courage)
3. **Get a coach**: Coaching and apprenticeship models accelerate growth
4. **Ensure sponsorship**: Secure trust and support from the right management level
5. **Keep improving**: Join a PO community; use retrospectives for feedback on own performance

### For Managers Developing Product Owners

1. **Recognize the role's importance**: PO role is the lynchpin of Scrum adoption (Schwaber)
2. **Select the right people**: Consider product, domain, and project size; staffing varies by company
3. **Empower and support**: Provide training, coaching, time, and decision-making authority
4. **Sustain the role**: Create development programs, career paths, PO communities; make organizational changes as needed

---

## Source

This summary was generated from the extracted text of "Agile Product Management with Scrum" by Roman Pichler (Addison-Wesley, 2010) on 2026-03-03. Content is organized by coaching use cases for AI agent consumption.
