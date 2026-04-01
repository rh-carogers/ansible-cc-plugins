---
source_type: gdrive
source_id: "1LKiSH-bpXZ-EQx3oHVdsTdem3HVJhrXjjLQL5ZM25P0"
source_name: "Ansible: Product Delivery Team backlog prioritization"
last_summarized: 2025-12-08
---

# Ansible: Product Delivery Team Backlog Prioritization - Summary

This document explains how Product Delivery Teams (PDTs) manage and prioritize their backlogs across different work types to achieve predictable delivery. Work comes from all sides, requiring teams to understand different work types, their sources, and how to effectively rank and manage them through sprint planning.

## Table of Contents

- [Core Principle: Team Ownership](#core-principle-team-ownership)
- [Work Flow and Sources](#work-flow-and-sources)
- [Sprint Planning Considerations](#sprint-planning-considerations)
- [Workstream vs Component](#workstream-vs-component)
- [Work Types: Detailed Breakdown](#work-types-detailed-breakdown) — escalations, CVEs, defects, features, RFEs
- [Product Delivery Team Board Backlog View](#product-delivery-team-board-backlog-view)
- [Data-Driven Decision Making](#data-driven-decision-making) — sprint reports, velocity, predictability
- [Understanding Value in Prioritization](#understanding-value-in-prioritization) — RICE, WSJF, story mapping
- [Jira Best Practices](#jira-best-practices) — dos, don'ts, consistency
- [Jira Hierarchy and Views Reference](#jira-hierarchy-and-views-reference) — ownership at each level
- [Release Strategy Considerations](#release-strategy-considerations)
- [Key Resources](#key-resources)

## Core Principle: Team Ownership

**The Product Delivery Team owns their backlog.** Talk happens everywhere, but work only comes through the backlog. Teams must understand:

- What work they are responsible for supporting (use JQL: `workstream OR component`)
- Board backlog as the primary view for prioritization, planning, and refinement decisions
- Different types of work and how to filter/view them effectively

## Work Flow and Sources

### Sankey Flow Diagram

Work flows into team backlogs from multiple sources with approximate percentages:

| Source | Percentage | Flow Path |
|--------|------------|-----------|
| **Strategic Features** | ~60% | Outcomes → Features → Team Backlog |
| **Initiatives** | ~15% | Outcomes/Other Initiatives → Team Backlog |
| **Customer RFEs** | ~5% | Direct → Team Backlog |
| **Customer Escalations/Bugs** | ~5% | Direct → Team Backlog |
| **CVEs** | ~5% | Direct → Team Backlog |
| **Continuous Improvement** | ~5% | Direct → Team Backlog |
| **Defects** | ~5% | Direct → Team Backlog |

### Business Flow Origins

Higher-level work originates from:

- **Ansible business needs/goals** → Outcomes
- **Red Hat Strategic Goals** → Outcomes
- **Outcomes** → Features (60%) and Initiatives (20%)
- **"Other" sources** → Additional Initiatives (10%) and Features (20%)

## Sprint Planning Considerations

When planning your sprint, consider:

- **The Ansible Unified Backlog** will show relative priority
- **"Long Poles in the Tent"** (critical path items)
- **Bugs/CVEs/Support Requests**
- **Tech Debt**
- **Other Urgent and Important items**
- **Conversations with the Outcome Leads**

**Key Insight:** This is a skill. You are planning 1 sprint at a time - if you're a little off, the risk is low.

## Workstream vs Component

| Field | Definition | Purpose |
|-------|------------|---------|
| **Component** | "What needs changes" | Identifies the codebase that requires modification |
| **Workstream** | "Who owns the work" | Identifies the delivery team responsible |

**Usage:** Use both fields. Teams are platform delivery teams who support one or many components. Assigning intentional "ownership" via Workstream signals to your team and other teams about who owns the work (prioritizing, planning, refining, estimating, demoing, delivering).

## Work Types: Detailed Breakdown

### Customer Escalations

**Purpose:** Just-in-time triage of customer escalations, collaborate with PM, Support, PXE. Provide regular updates.

**JQL Queries:**

- `labels IN (ansible-prio)`
- `"SFDC Cases Links" is not empty`

**Supporting Views:**

- Customer Issues Dashboard
- Escalation Kanban board

**Weekly Actions:**

- During daily standup: address new escalations, follow up on needed information
- Determine trade-offs to include in current sprint
- Use priority, severity, customer case links to Rank against other work in Team Backlog

**Resources:**

- Escalations process
- Issue Use Guide
- #aap-911 Slack channel
- RCA folder

### CVEs

**Purpose:** Continuously triage CVE trackers (type: Vulnerability). Must be part of bug triage ceremony and prioritized over feature work when applicable - remember what customers are paying us for.

**JQL Queries:**

- `issueType in (Vulnerability, Weakness) OR (issueType IN (Bug) and labels IN (SecurityTracker))`

**Supporting Views:**

- CVE Dashboard
- CVEs Knowledge Base

**Weekly Actions:**

- Review the CVE Dashboard
- Filter by component(s) your team supports
- Update any needing attention to ensure they show up correctly in team backlog (status, sprint value)
- Use Due Date, Severity to Rank against other work in Team Backlog

**Resources:**

- Issue Use Guide
- JQL + Views documentation

### Quality & Stability (Defects)

**Purpose:** Continuously triage Defects (type: Bug) in daily standup, refinement, or regular bug triage ceremony.

**JQL Queries:**

- `issueType = Bug`
- `"SFDC Cases Links" is not empty`
- `affectedVersion IN` or `affectedVersion =`

**Supporting Views:**

- Defects Dashboard
- Bug Triage Knowledge Base
- How to file a Bug Knowledge Base

**Weekly Actions:**

- Review the Defects Dashboard
- Filter by component(s) your team supports
- Update any needing attention for team backlog visibility (status, sprint value)
- Identify high priority/customer impacting bugs and rank higher in backlog
- Use Priority, Severity, Customer Impact (PX Prio, SFDC Cases) to Rank against other work

### Strategic Features/Initiatives (Level 4)

**Purpose:** Regularly refine Features/Initiatives by designing and decomposing into phased delivery via epics and rank against other Features/Initiatives.

**JQL Queries:**

- `issueKey in childIssuesOf("FEATURE-123")`
- `issueKey in childIssuesOf("OUTCOME-123")`
- `component IN (continuous-improvement)`
- `labels IN (tech-debt)`
- `issueKey IN childIssuesOf("INITIATIVE-123")`

**Supporting Views:**

- Ansible Unified Backlog
- KR2 gadget 1 and 2 (for continuous improvement)

**Weekly Actions:**

- Ensure Feature/Initiative work is decomposed into Epics/Stories/Spikes ready for team backlog sprint refinement/planning
- Use rank of parent Feature/Initiative to inform how to rank Epics/Stories/Spikes against other work types
- Consider: priority, "value", linked issues (dependencies)

**Additional Resources:**

- Ansible Feature Delivery
- Decomposing Features
- Rank (slides 32-33)
- Issue Use Guide

### RFEs (Request for Enhancement)

**Purpose:** Continuously triage/refine RFEs during Delivery team 3-in-the-box conversations.

**JQL Queries:**

- `issueKey in childIssuesOf("ANSTRAT-958")`
- `labels IN (RFE)`

**Supporting Views:**

- RFE Prio List

**Weekly Actions:**

- Review RFE Prio List with Delivery team 3itb
- Determine: Do we need to prioritize a spike? Do we have capacity? What's the scope (Feature, Epic, Story)?
- Rank actions needed and work with PM to add comments signaling next steps/updates to requestor
- Use Priority, Severity, Customer Impact (PX Prio, SFDC Cases) to Rank against other work

**Resources:**

- RFE Process

## Product Delivery Team Board Backlog View

### Key Elements for Ranking

**Epic Panel:**

- Helps organize/rank work across multiple Features/Initiatives for current/upcoming sprint
- Rank = relative priority

**Refinement Status:**

- Focus on work needing refinement to reach "ready to work" state
- Can be considered for future sprint or during sprint planning

**Future Sprint(s):**

- Create these to "schedule" work we know we need to do next
- Assumes work is "ready to work" (has been triaged/refined)

**Current "Active" Sprint:**

- Work committed to getting "DONE" in our sprint
- Consider work that is "ready" to help be predictable

## Data-Driven Decision Making

### Sprint Reports for Retrospectives

| Report Type | Key Questions |
|-------------|---------------|
| **Sprint Report/Burndown Chart** | Did we achieve our goal? How much did our sprint get interrupted? Did we commit to "too much"? |
| **Velocity Chart** | Use during next sprint planning to gauge how much work to commit to |
| **Work Type Dashboard** | Are we focusing "too much" on one type of work and "not enough" on another? Helps rank/balance backlog for next 1-3 sprints |

### Predictability Equation

**Completed Pointed Sprints + Work Type = Predictability**

### Why "work type" is important
As Ansible Engineering, we need to understand where our work effort is being spent so we can communicate with stakeholders, make informed investment decisions, and make reasonable commitments.

### Ansible OKRs

**2024 OKR Achievement:**

- **Goal:** Size all applicable work
- **Status:** Overwhelmingly met objectives
- **Impact:** Provided first part of "predictability equation"

**2025 OKR:**

- **Goal:** Classify all applicable work with "Work Type"
- **Treatment:** Work without work type will be treated as hygiene issue
- **Impact:** Enable communication with stakeholders, informed investment decisions, and reasonable commitments

## Understanding Value in Prioritization

### Value-Driven Decision Making

**Key Questions:**

- How much revenue is tied to something?
- How many customers are impacted?
- How else do we quantify "value"?

**Methods:**

- **RICE** (Reach, Impact, Confidence, Effort)
- **WSJF** (Weighted Shortest Job First)
- **User story mapping**

**Example Bug Scenario:**

- 1 bug impacting 100 customers (even if low priority)
- 100 customers currently working around the issue
- Knowing the number (100) enables more accurate decision-making

## Jira Best Practices

### Three Important Concepts

1. **Statuses + Workflows:** What activities happen to get work from "new" to "done" - replaces need for status reports and meetings
2. **Project + Issue Types:** Tells us "what" needs to get done and "who" is involved - different levels help scale communication
3. **Rank:** How we incorporate different work types into a single list (now vs next up) - intentional activity at multiple levels

### Jira Dos and Don'ts

**Do:**

- Learn and regularly manage "Rank" - tells us what to work on right now and next-up
- Leverage status to reflect current state and communicate what else needs to happen to move to done
- Write issues where "the why" and value delivered is clear, regardless of who does it
- Think about "why", "what", "who" when thinking about views - the view should support the discussion and participants
- Use filters for one-time or ad hoc filtering to solve immediate problems

**Don't:**

- Build processes off labels
- Rely on Filters - may be hiding a "gap" we should identify and correct. Clean up the backlog (tag the work), don't filter around it
- Default to decomposing issues based on how we organize internally (based on "who" or function like Dev vs QE)
- Default to creating new views, fields, or labels - try to understand what's there and why first

### Consistency is Key

Communication with less mental math requires consistency in how we use Jira across teams and projects.

## Jira Hierarchy and Views Reference

### Business Priorities (Outcomes Level)

| Aspect | Details |
|--------|---------|
| **Owner** | Eng and BU leadership |
| **Creator** | BU |
| **Signoff** | Sathish, Xav, Kevin |
| **Views** | Ranked Outcomes, Ranked New Features List |
| **Filter** | 1) Unified backlog Level 5 > Level 4; 2) Features with Status = New |
| **Forum** | QBR and Monthly sync |
| **Purpose** | Are we making incremental progress on business goals? Do we need to change prioritization or make trade-offs based on results? |

### Product Design Priorities (Features Level)

| Aspect | Details |
|--------|---------|
| **Owner** | PM Leads |
| **Creator** | PM / Arch |
| **Signoff** | Eng and BU leadership |
| **View** | PM/Tech Lead Interlock |
| **Filter** | Features with Status IN (Refinement, Backlog) |
| **Forum** | Bi Weekly Leads, Bi Weekly PM, Eng/Product Sync |
| **Purpose** | What features do we need to design and get ready for implementation? Define acceptance criteria, scope, delivery plan. May need trade-offs based on scope/resourcing. |

### Delivery Team Priorities (Epic and Below)

| Aspect | Details |
|--------|---------|
| **Owner** | PM and Delivery Manager |
| **Creator** | PM and Engineering |
| **Signoff** | PM & Engineering Manager |
| **View** | Team Scrum Board |
| **Filter** | Based on Project, Component, Workstream |
| **Forum** | Delivery team ceremonies (Sprint level, Scrum of Scrums, 3-in-the-box) |
| **Purpose** | Are we making progress on commitments? Are we blocked? Do we need to add/remove scope, swarm, or do additional design/refinement? |

## Release Strategy Considerations

### Current State Assessment

**Keep (Good Stuff):**

- Accountability
- 3-in-the-box partnership
- Velocity of decision making

**Improve:**

- **Roles and expectations:** Continue with L2/L3? Return to Collaborative Delivery/"agile" roles? Combination/mapping?
- **Delivery teams:** Align on teams and what they support (affects work tracking and backlog building)
- **Priority flow:** Priorities flow through teams' backlogs - don't form teams around priorities
- **Release approach:** Shift from Fixed Date/Fixed Scope to ranked priorities shipped when ready

### Proposed Improvements

- **Target End Date:** Only at Feature/Initiative level; for lower level work, think timeboxed iterations (sprints)
- **Ranked backlog:** Use instead of filtered backlog based on fix version
- **Fix version usage:** Apply when something is MERGED, not before

## Key Resources

- [Issue Use Guide](link)
- [Unified Backlog References](link)
- [Sankey Diagram Tool](https://sankeydiagram.net/) (for visualizing work flow)
- #aap-911 Slack channel (for escalations)
- Various Knowledge Bases: CVEs KB, Bug Triage KB, How to file a Bug KB
