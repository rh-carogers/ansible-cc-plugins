---
source_type: gdrive
source_id: "1gl0cj4RyMuQ7TSd8hIqXFrHXsvMt10nd-fTg30CQncA"
source_name: "Ansible: Jira Issue Use Guide"
last_summarized: 2026-04-01
---

# Ansible Jira Issue Use Guide - Summary

This guide provides distinctions between issue types in the Ansible hierarchy and addresses common areas of confusion between issue types. It builds upon Red Hat Standards to provide additional context specific to Ansible, helping teams understand when and how to use each issue type effectively.

## Issue Type Hierarchy Overview

The Ansible team follows a 6-level hierarchy for organizing work:

| Level | Issue Type    | Purpose                                             | Creator                | Assignee                       | Estimated?    | PR Required? |
| ----- | ------------- | --------------------------------------------------- | ---------------------- | ------------------------------ | ------------- | ------------ |
| 6     | Strategic Goal | Company strategic goals                             | Leadership             | VP/Engineering Executive       | No            | No           |
| 5     | Outcome       | Customer/stakeholder benefit                        | Leadership             | Product/Engineering Director   | No            | No           |
| 4     | Feature       | Specific customer-facing functionality              | Product Manager        | Product Manager                | Size (rollup) | No (rollup)  |
| 4     | Initiative    | Specific engineering/org functionality              | Engineering            | Staff Engineering / Architect  | Size (rollup) | No (rollup)  |
| 3     | Epic          | Large user story for single team                    | 3-in-Box/Product Owner | Team member                    | Size (rollup) | No (rollup)  |
| 2     | Spike         | Time-boxed research activity                        | Epic Lead              | Team member                    | Story Points  | No           |
| 2     | Story         | Unit of work delivering value in a single sprint    | Epic Lead              | Team member                    | Story Points  | Yes          |
| 2     | Task          | Finite action or customer escalation                | Anyone                 | Team member                    | No            | No           |
| 2     | Bug           | Product defect, unplanned work                      | Anyone                 | Team member                    | No            | Yes          |
| 2     | Vulnerability | Exploitable security issue in Red Hat product       | Product Security       | Team member                    | Story Points  | Yes          |
| 2     | Weakness      | Security weakness (no actual exploit) in product    | Product Security       | Team member                    | Story Points  | Yes          |
| 2     | Risk          | Potential hazard preventing desired results         | Anyone                 | Assignee                       | No            | No           |
| 1     | Sub-task      | Single unit breakdown                               | Team/Story Owner       | Team member                    | No            | No           |

## Strategic Goals (Level 6)

**Purpose:** High-level value goals for the company achieved through multiple factors

**Key Characteristics:**

- Spans multiple Outcomes, may require multiple years (max 5 years)
- Located in Product Strategy (HATSTRAT) Jira project
- Owned by BU VP and Engineering Executive
- Each Strategic Goal has a champion (assignee) responsible for the what/why and a designer responsible for the how/when
- Completion means achieving business/value targets through tangible outcomes

**Example Results:** Increased Single Year Booking by X%, added product offering with Y new customers, increased retention rate by Z%

## Outcomes (Level 5)

**Purpose:** Observable/measurable changes in human behavior that drive business results

**Key Characteristics:**

- Spans multiple releases, may take over a year
- Located in ANSTRAT (Product-Specific Strategy) project
- Connects roadmap deliverables to corporate strategy
- Assignee accountable (Product Management, Engineering Management, or Change Leader)

**Completion Criteria:** Know whether deliverables changed human behavior and created desired business results through observation/measurement

## Features & Initiatives (Level 4)

| Aspect        | Features                                        | Initiatives                                                    |
| ------------- | ----------------------------------------------- | -------------------------------------------------------------- |
| **Purpose**   | Tangible customer value delivered incrementally | Architectural/improvement goals with clear completion criteria |
| **Scope**     | Single release, single product area             | ~6 months or single release, single area                       |
| **Ownership** | Product Manager                                 | Engineering/Product Management                                 |
| **Delivery**  | Creates customer capability                     | Creates Red Hat associate capability                           |
| **Location**  | ANSTRAT project                                 | ANSTRAT project                                                |

**Common Confusion:** Not intended to cross multiple releases (solution: split into multiple Features/Initiatives and, as needed, create an Outcome). Not a group of "all other" Epics for a single team (solution: Epics are not required to have a parent; use components/labels to group work).

## Risks (Level 2)

**Purpose:** Something that constitutes a potential hazard that could prevent achieving desired results. Used in Jira to bring broad transparency to a situation and foster collaborative efforts to address it.

**Key Characteristics:**

- Scope spans the duration of the issue impacted by the Risk
- Not typically sized
- Located in ANSTRAT project, linked to related Features, Initiatives, Epics, Tasks, Stories, Bugs via issue links
- Linked using "issue links" and **not** as parent/child relationships

**Completion:** Risk has been addressed (action taken to mitigate/resolve, or the prompting issue is now complete and the Risk is no longer applicable)

## Epics (Level 3)

**Purpose:** Extra-large stories with functionality descriptions and Acceptance Criteria

**Key Characteristics:**

- Larger than single sprint, smaller than release
- Often single team scope, may span multiple teams
- Sized using T-shirt sizes
- Located in delivery team projects (AAP, ACA, ANA, PARTNERENG, ANSCORE)

**Completion:** Acceptance Criteria met, work demo'd to stakeholders

**Common Confusion:** Not intended to remain open permanently to group work (solution: use Components or Labels)

## Planned/Proactive Work (Level 2)

### Stories

- **Purpose:** Capability description from user perspective
- **Size:** Single sprint, single team, sized in story points
- **Completion:** Acceptance Criteria met, work demo'd

### Spikes

- **Purpose:** Time-boxed research for better decisions
- **Size:** Sized in story points; no PR/code change
- **Completion:** Time-box met, decision made, resulting Stories written. Demo could be valuable to share learnings.

### Tasks

- **Purpose:** Finite piece of work, great for post-meeting follow-ups and action items
- **Size:** Not required to estimate, but encouraged if it helps with predictability
- **Completion:** Action complete, no PR/code change required
- **No demo needed**

### Vulnerability & Weakness

- **Creator:** Product Security only (filed in AAP project only)
- **Purpose:** Security issues (Vulnerability = exploitable, Weakness = no actual exploit)
- **Size:** Not required to estimate, but encouraged if it helps with predictability; use Points
- **Completion:** Addressed via code change or decision to defer/close, updated with appropriate resolution and status by SLA/Due Date
- **No demo needed**

## Unplanned/Reactive Work (Level 2)

### Bugs

- **Purpose:** Error, flaw, or fault in software causing incorrect results
- **Scope:** Goal is single sprint, may take longer
- **Size:** Not required to be sized, but can use Points if helpful for the team
- **Hierarchy:** Level 2, linked to Epics via "issue links" (not parent/child)
- **Location:** AAP project for customer issues; delivery team projects for other defects
- **Completion:** Problem fixed, code merged/released

### Escalations (Tasks)

- **Purpose:** Customer requests requiring immediate attention
- **Process:** May result in linked Bug or Story for code changes
- **Completion:** Escalation resolved, customer communication provided. Log actual time spent when relevant.

## Sub-tasks (Level 1)

**Purpose:** Specific actions to complete larger issues (Story, Spike, Task)

**Key Characteristics:**

- Few days maximum scope
- Single person assignment
- Not required but useful for clarity
- Inherit values from parent issue (sprint value, security level, etc.)
- Consider whether to use sub-tasks or decompose into additional stories/spikes/tasks

**Examples:** Code written, unit tests passed, PR review complete

## Project Locations

- **HATSTRAT:** Strategic Goals
- **ANSTRAT:** Outcomes, Features, Initiatives, Risks
- **Delivery Teams (AAP, ACA, ANA, PARTNERENG, ANSCORE):** Epics, Stories, Spikes, Tasks, Bugs, Sub-tasks
- **AAP Project:** Customer Bugs, Vulnerabilities, Weaknesses (created by Product Security)

## Key Principles

1. **Size Appropriately:** Each level should fit its intended scope
2. **Use Components/Labels:** For grouping work, not permanent parent issues
3. **Demo Work:** Stories and Epics require stakeholder demos
4. **Time-box Spikes:** Research has defined end points and outcomes
5. **Link Don't Parent:** Use issue links for Bugs and Risks instead of parent/child relationships

## Common Pitfalls to Avoid

- Strategic Goals are not corporate strategy itself
- Outcomes should specify behavior changes and measurements, not just deliverable lists
- Features/Initiatives shouldn't cross multiple releases
- Epics shouldn't remain open just to group work
- Stories/Spikes/Tasks shouldn't roll over multiple sprints
- Sub-tasks aren't required - use them only when helpful for clarity
