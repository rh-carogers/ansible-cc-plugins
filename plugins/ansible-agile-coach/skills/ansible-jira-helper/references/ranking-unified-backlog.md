---
source_type: gdrive
source_id: "1C3bG-3VNvWbAyDmNSHis1uhH0K4KbvHGKSnFPUqXbfw"
source_name: "Ranking the Unified Backlog"
last_summarized: 2025-12-08
---

# Ranking the Unified Backlog - Summary

This document explains how to rank work items in the Ansible Unified Backlog at two organizational levels: Product/Offering level (Features and Initiatives) and Delivery Team level (Epics and below). Proper ranking ensures teams understand relative priorities and can make informed decisions about what to work on next.

## Product/Offering Level (Features, Initiatives)

### Purpose

Rank Features across all Outcomes relative to each other from the perspective of the current and next release.

### Who is Involved

**Responsible:**

- PMs, Directors, Staff Engineering Leads
- [Feature Leads](https://docs.google.com/presentation/d/1r8tgHoTdy0TIgHh44rioWLqRDrETVXdekawsVyjuePc/edit#slide=id.g202a89820f8_1_766) (for current features being refined/implemented)

**Informed:**

- Each delivery team should be aware of relative priority of Features, specifically the Features their team supports
- This awareness enables teams to effectively rank their team backlog and sprint backlog

### When to Rank

- **Ad hoc sessions:** As needed to reflect next up release(s) (quarterly)
- **Ongoing:** Every other week Feature refinement (on the off week of sprint start/end, so teams have time to refine and coordinate)
- **PM team suggestion:** Look regularly at 'new' features, reflect Rank and when ready move to Refinement

### How to Rank

**Primary Method:**

- Use [Ansible Unified Backlog](https://issues.redhat.com/secure/PortfolioPlanView.jspa?id=1167&sid=1167&vid=9849#plan/backlog) with limited permissions
- Rank "above issue" or "below issue" to ensure consistency if issues are present in multiple plan views

**Additional Plan Views:**

- If using additional [plan views](https://issues.redhat.com/secure/Dashboard.jspa?selectPageId=12363497#Rich-Text/12471825) (scoped to focus area or team)
- Work with PM and Staff Eng lead to communicate Level 4 rank changes via #ansible-program
- Tag Feature leads and Outcome leads for visibility

### Common Ranking Scenarios

**Scenario A - Dependency Management:**

- While refining a feature, identify a dependency
- Need to move that dependency (another Feature or Initiative) above the current feature (higher rank)

**Scenario B - Capacity Constraints:**

- Delivery Team A must support 5 features but only has capacity for 3
- Rank top 3 as highest priority to plan and release them
- As progress is made, move to features 4 and 5
- This approach helps decide whether to:
  - Focus additional teams on top features for faster delivery
  - Have teams prioritize other work until capacity is available
  - Adjust delivery plans accordingly

**Key Principle:**
Use Ranked Outcomes to inform Ranked Features, in addition to dependencies, release plan, and capacity. Partnership between PM lead, Staff Eng Lead, and Director is essential.

## Delivery Team Level (Epic and Below)

### Team-Level Purpose

Understand what to work on next by reflecting relative priority of [different types of work](https://docs.google.com/presentation/d/1LKiSH-bpXZ-EQx3oHVdsTdem3HVJhrXjjLQL5ZM25P0/edit#slide=id.g30e690bb658_0_105) for each sprint:

- High priority escalations or CVEs
- Multiple Strategic Features
- Continuous improvement work

### Team-Level Roles

**Delivery Team 3-in-the-Box** (PM, Engineering Manager, Tech Lead) = "Product Owner"

- Collectively accountable to deliver the team's backlog
- Responsible for ranking daily/weekly/per-sprint

### Epic Lead

- Member of delivery team responsible for coordination, communication, refinement, delivery of an epic
- Communicates with Feature Leads and Delivery team 3itb
- Represents updates/progress on behalf of team at Scrum of Scrums (SoS)

### Team Ranking Schedule

**Minimum:** Weekly leads call including:

- Delivery team 3itb
- Feature Leads of each Feature the team is currently working on

**Ad hoc/As needed/Daily:**

- Rank to adjust new bugs, new stories, new spikes created
- If team has dedicated/rotating "Scrum Master" or "Scrum Leader":
  - Work with Delivery Team 3itb to prepare backlog for Refinement (status = Refinement)
  - Prepare backlog for Planning (status = Backlog)
  - Stay on top of "new" unplanned work (status = New and type = Bug)

### Team Ranking Methods

**Core Principle:**

- **A team owns their backlog: Epic and below**
- **Use Workstream field to clarify team ownership**

**Method:**

- Follow [Ansible: predictable feature delivery](https://docs.google.com/presentation/d/1ijU_UITun28tJKc6Vae9MmMcdvgEx4tdBaEkyXthZr8/edit#slide=id.g313aeb1c21a_0_5471) using Feature Rank to inform Epic and sprint level rank

**Two Ways to Rank Epics Across Features** (different UX, same results):

1. **Team board backlog:** [Ansible: Product Delivery Team backlog prioritization](https://docs.google.com/presentation/d/1LKiSH-bpXZ-EQx3oHVdsTdem3HVJhrXjjLQL5ZM25P0/edit#slide=id.g30b7b7b3e82_0_9)
2. **Ranked Epics in plan view:** [Ansible: predictable feature delivery](https://docs.google.com/presentation/d/1ijU_UITun28tJKc6Vae9MmMcdvgEx4tdBaEkyXthZr8/edit#slide=id.g313aeb1c21a_0_5953)

## Known Impediments

### Communication

**Key Principles:**

- Jira **does not** replace human interaction - it documents conversations
- Don't default to "process and tooling" - understand what you're asking and why
- Have conversations first, then reflect decisions in the tool
- Use hygiene dashboards to highlight accountability

**Feature Lead Responsibilities:**

- **Proactively communicate** with anyone involved with their feature throughout the lifecycle
- **Reflect decisions, agreements, and shared understanding** in the Feature including:
  - Acceptance Criteria
  - Rank
  - People fields
  - Components
  - Status
  - Child issues
  - Issue Links (dependencies)

### Hygiene

**Purpose:** Data helps make decisions. Without accurate data, conversations lack proper anchoring.

**Guidance Resources:**

- [Issue Use Guide](https://docs.google.com/document/d/1gl0cj4RyMuQ7TSd8hIqXFrHXsvMt10nd-fTg30CQncA/edit?tab=t.0#heading=h.px02ldo06nsg)
- [Knowledge Base](https://spaces.redhat.com/x/IjlHG)
- [Collaborative Delivery](https://docs.google.com/presentation/d/1r8tgHoTdy0TIgHh44rioWLqRDrETVXdekawsVyjuePc/edit#slide=id.g547716335e_0_260)
- [Feature Delivery](https://docs.google.com/presentation/d/1ijU_UITun28tJKc6Vae9MmMcdvgEx4tdBaEkyXthZr8/edit#slide=id.g313aeb1c21a_0_5471)

**Common Hygiene Checks:**

**Release Health (Product/Offering Level - Features/Initiatives):**

- [Features in Refinement](https://issues.redhat.com/secure/Dashboard.jspa?selectPageId=12364519#Rich-Filter-Two-Dimensional-Statistics/12495365) missing ["New" Exit Criteria](https://docs.google.com/presentation/d/1r8tgHoTdy0TIgHh44rioWLqRDrETVXdekawsVyjuePc/edit#slide=id.g2600e58d299_0_0)
- [Features in Progress](https://issues.redhat.com/secure/Dashboard.jspa?selectPageId=12364519#Rich-Filter-Two-Dimensional-Statistics/12478872) missing ["Refinement" Exit Criteria](https://docs.google.com/presentation/d/1r8tgHoTdy0TIgHh44rioWLqRDrETVXdekawsVyjuePc/edit#slide=id.g2ec47bafa14_11_0)
- **Stale Features:** [ANSTRAT Features in progress > 6 weeks, no update in 4 weeks](https://issues.redhat.com/issues/?filter=12453807)
- **Recent Changes:** [Features exiting Refinement in the last week](https://issues.redhat.com/issues/?filter=12453381)

**Team Level (Epic and Below):**

- [Hygiene Dashboard](https://issues.redhat.com/secure/Dashboard.jspa?selectPageId=12354609)

### Role Accountability/Consistency

**Important:** Know your role and the level of "what" you are talking about. You may wear different hats:

- **Outcome lead**
- **Feature lead**
- **Delivery team member**
- **Delivery team 3itb**
- **Leadership** (accountable)
- **Combination of the above**

**Key Mindset:**

- We are building muscles - change is hard, we won't get it right at first
- Be curious and assume good intent
- Don't be afraid to hold someone accountable - understand why and help be part of solutions

## Key References

- [Unified Backlog References](https://issues.redhat.com/secure/Dashboard.jspa?selectPageId=12363497#)
- [Ownership at Different Levels](https://docs.google.com/presentation/d/1ijU_UITun28tJKc6Vae9MmMcdvgEx4tdBaEkyXthZr8/edit#slide=id.g313aeb1c21a_0_5914)
- [Panel from Dec All Hands](https://drive.google.com/file/d/1HXhBXejHU0S1FNviFU0Akk5XdLScy_8E/view?usp=sharing)
- [Ansible Engineering All Hands - 2024Dec12](https://docs.google.com/presentation/d/1Rc7VVfBtEWiSeNqLOWAATPvzn_7-fqWnkIIYtILal8k/edit#slide=id.g2d69888b2a8_0_27)
- [Ansible Staff Engineering Weekly - 2025/01/30 Recording](https://drive.google.com/file/d/1PkJWKZvWev528eA4N5Y6KyDZ6EMVF-O-/view) (Roles, Views, Ceremonies)
