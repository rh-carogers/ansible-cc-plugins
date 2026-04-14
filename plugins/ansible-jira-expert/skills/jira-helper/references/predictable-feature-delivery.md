---
source_type: gdrive
source_id: "1ijU_UITun28tJKc6Vae9MmMcdvgEx4tdBaEkyXthZr8"
source_name: "Ansible: predictable feature delivery"
last_summarized: 2025-12-08
---

# Ansible: Predictable Feature Delivery - Summary

This document outlines the approach to improving Feature backlog management for predictable delivery in Ansible, presented by Heather Smith, Enterprise Coach in Ansible. The focus is on leveraging the unified backlog to create an accurate, prioritized system that provides clarity around roles, ownership, and data-driven release health.

## Goal: Improve Our Feature Backlog

Create an accurate, prioritized backlog that:

- Shows the current and next releases for our product/offerings
- Provides clarity around roles and ownership to help scale communication and make decisions faster
- Enables data-driven release health based on agreed-upon "signals"

## Current Situation: The Problem We're Solving

**Common Pain Points:**

- "What are the next up priorities?"
- "We are doing too much at once"
- "How are we progressing?"

**Impact of Uncertainty:**
Lack of clarity and consistency creates uncertainty, which leads to:

- Burnout
- Change fatigue
- High workloads/"hero culture"
- Excessive status reporting and meetings

**Solution Approach:** Rather than trying to impact all factors at once, focus on one step: improving our unified, transparent, and prioritized Feature backlog.

## Roadmap Mindset Transformation

### From Misleading to Strategic Roadmaps

| Roadmap Type | Characteristics | Timeline Focus |
|--------------|-----------------|----------------|
| **Misleading Roadmap** | "We will follow this linear path from zero to our inevitable victory, and these are the milestones that will get us there." | What will we release in 12 months |
| **Honest Roadmap** | "We know where we are today, and have a good idea about the near future, but recognize that the future becomes uncertain." | What will we release throughout the year |
| **Strategic Roadmap** | "We know where we are today, and anticipate decision points that will change our path. We are intentionally gathering the data that will help us make decisions." | What will we release the next few sprints |

**Key Transformation:** Reframe from large 6-12 month release backlogs toward more incremental planning and delivery, with Outcomes describing the range of business goals.

## Foundation Requirements

### What We Need for Success

1. **Consistency** in how we model Outcomes + Features
2. **A ranked backlog at all levels** including a Ranked Feature backlog that shows current + next releases
3. **Alignment on our release strategy:** what we release and when
4. **Clarity of ownership** (how we tag work)

*Note: These three inputs are foundational to OpenShift's "Feature Analysis Tool", enabling them to predict timeframes and releases.*

## Outcomes vs Features: Clear Definitions

| Type | Definition | Scope | Timeline |
|------|------------|-------|----------|
| **Outcome** | A business goal with clear success criteria that we work to achieve over multiple releases/"quarters" via the delivery of our Features/Initiatives | May cross multiple product/offerings | 3-12 months |
| **Feature** | Specific functionality, a tangible piece of value, a deliverable that is scoped to a single "release" or phase (e.g., MVP released to cloud first, "Phase 2" on AAP behind feature flag, fully GA on AAP) | Scoped to a single product/offering | Single release/phase |

**References:**

- [Ansible Jira Issue Use Guide](https://docs.google.com/presentation/d/1r8tgHoTdy0TIgHh44rioWLqRDrETVXdekawsVyjuePc/edit#slide=id.g23768f8478f_0_2)
- [Ansible Unified Backlog Ranked Outcomes View](https://docs.google.com/presentation/d/1RxTB2RYUSFAzCWYnmM56pDxcpqWydpRQ0Kf6c7PxDos/edit#slide=id.g267d2db082f_0_59)

## User Stories: Roles and Expectations at Strategic Layer

### Senior Leadership

**As a member of Senior Leadership:**

- **Need:** Updates from Outcome leads to understand progress and success criteria
- **Purpose:** Accurately present strategic direction, investments, and progress to leadership team; influence direction when needed

### Outcome Lead

**As an Outcome Lead:**

- **Need:** Identify what Features/Initiatives we start next (rank) and who will help drive them (leads) across and within Outcomes
- **Need:** Updates from Feature Leads to understand progress and where trade-offs are required to meet business needs (rank)

### Feature/Initiative Lead

**As a Feature/Initiative Lead:**

- **Need:** Work with Feature team (often >1 delivery teams) to plan and deliver product with platform mindset (collaborative delivery framework)
- **Need:** Coordinate with Feature Leads/Delivery teams across Outcomes/Features to align on dependencies and priorities so teams can make accurate trade-offs per Sankey (rank)

## Ranked Backlog Implementation

### Enabling Ranking at All Levels

**Core Principle:** Enable 3-in-the-Box (3itb) to rank their team's backlog (Epic and below) based on Ranked Features

**Process:**

1. **Regularly refine** Features/Initiatives and decompose into phased delivery via Epics/Stories/Spikes
2. **Rank** the Epics/Stories/Spikes against other features and work types by considering the parent's rank
3. **Reference:** Rank 101 slides 32-33 for detailed guidance

## Release Strategy Alignment

### Release Types and Customer Consumption

**Cloud-Based Products:**

- AoC SaaS, AoC Azure, Lightspeed, Content have milestones
- Customers always consume the latest version

**On-Premise Products:**

- AAP is on-premise with supported versions
- Customers must upgrade/migrate between versions

### Release Cadence Strategy

**"Sprint Level" Releases:**

- Ensure build health quality
- Provide feedback early and often

**"Feature Level" Releases:**

- Represent marketable, supported piece of functionality
- Coordinate across the product/offering

## Tooling to Support Release Strategy

### Version Management in Jira

Assuming we have a ranked Feature backlog and ranked team-level backlogs:

| Version Field | Purpose | Usage |
|---------------|---------|--------|
| **Affects Version** | For bugs | AAP major version OR "latest" for cloud |
| **Target Version** | Planning tool for committed work | Used for work in a sprint |
| **Fix Version** | Reflects actual release version | Updated when work is actually released |

### Planning Tools

**Candidate Labels:**

- Used by PM and leadership as planning tool
- **Important:** Does not signal commitment on its own
- 3-in-the-Box must discuss and rank in team backlog

### Program Level Dashboards

**Release Health Dashboard:** How are we progressing
**Release Blockers Dashboard:** What is stopping us from being able to release today

## Clarity of Ownership

### Hierarchy and Decision-Making Levels

Each level in the hierarchy represents different levels of ownership/decision making:

| Level | Owner | Responsibility |
|-------|-------|----------------|
| **Outcomes** | Outcome Leads | Responsible for reporting out/reporting up on overall goals, including delivery of all features within the Outcome(s) backlog |
| **Features** | Feature Team | Responsible for refining, decomposing, and delivering Feature, including coordinating across teams when needed |
| **Epics and Below** | Delivery Team (3-in-the-Box) | Responsible for prioritizing, planning, and delivering a team's backlog, which can be made up of multiple Features (via Epics) and work types (CVEs, Defects, Stories, etc.) |

### Jira Field Usage for Ownership

| Field | Outcome Level | Feature Level | Epic and Below |
|-------|---------------|---------------|----------------|
| **Assignee** | BU Leader or Eng Director | Product Manager | Team member (IC) |
| **Architect** | DE or Sr PE | Sr PE or PE or Tech Lead | n/a (Team collectively owns; use Contributors field if helpful) |
| **Developer** | Director | Eng Manager or IC | Engineering representative (development/testing/docs) |
| **Workstream** | n/a | n/a | Delivery team responsible for refining, planning, and delivering |

*Note: At the execution layer, ownership transitions from "leads" to "delivery teams." Architect and Developer fields are used at Outcome/Feature level; Workstream + Assignee fields are used at Epic and below.*

**References:**

- [Ansible: How we tag work in Jira](link)
- [Feature Team reference](link)
- [Delivery Team reference](link)
- [Hierarchy reference](link)
- [OCP "outcome team" reference](link)

## Sample Jira Views for Different Ownership Levels

### 1. Ranked Outcomes View

**Purpose:** Support overall state of business goals

**Shows:** Overall business goals in order of relative priority
**Question Answered:** "What are we trying to do (bigger picture) as a business/product and how are those larger (often multi-release goals) going?"

**Key Fields:** Status, Assignee/Architect/Developer (Outcome leads), Progress, Target End

### 2. Ranked Features View

**Purpose:** Support release planning

**Shows:** Overall Features in order of relative priority for current and next release
**Question Answered:** "What are we doing with the product/offering?"

**Key Fields:** Status, Assignee/Architect*/Developer* (Feature leads), Workstream (team ownership), Progress, Dependencies

### 3. Ranked Epics View

**Purpose:** Support execution layer progress and ownership

**Helps:**

- Outcome/Feature leads stay clear on "who" is doing what, how/where to delegate, how/where to make resourcing decisions
- Teams rank work across features in order of relative importance to prep for sprint planning

**Includes:** Issue types and fields geared towards "execution" (Epic and below) and progress (is stuff in a sprint yet?)

**Key Fields:** Status, Assignee, Workstream, Sprint, Progress, Dependencies

## Key References

- [Ansible Unified Backlog Ranked Outcomes View](https://docs.google.com/presentation/d/1RxTB2RYUSFAzCWYnmM56pDxcpqWydpRQ0Kf6c7PxDos/edit#slide=id.g267d2db082f_0_59)
- [Collaborative Delivery Framework](https://docs.google.com/presentation/d/1r8tgHoTdy0TIgHh44rioWLqRDrETVXdekawsVyjuePc/edit#slide=id.g23768f8478f_0_2)
- Decision logs for Ansible release strategy
- OCP Sample implementation for tooling reference
