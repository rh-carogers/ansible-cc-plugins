# Story Mapping — Coaching Reference

Based on Jeff Patton's "User Story Mapping" approach. Use this reference when coaching
teams on story mapping workshops, release planning through maps, or visualizing the
big picture of a product.

---

## What Story Mapping Is

Story mapping is a technique for arranging user stories into a useful model that helps
understand the functionality of the system, identify holes and omissions, and effectively
plan releases that deliver value to users with each release.

The key insight: a flat backlog loses context. You can see individual stories but not how
they relate to each other or to the user's journey. A story map restores that context by
organizing stories in two dimensions.

## The Two Dimensions

### Horizontal: The Backbone (User Activities and Tasks)

The top of the map tells the story of the user's journey from left to right:

```
[Activities]    Browse Products  →  Add to Cart  →  Checkout  →  Track Order
                     |                  |              |             |
[User Tasks]    Search by name     View cart      Enter address   View status
                Filter by price    Update qty     Choose payment  Get updates
                View details       Remove item    Confirm order
```

- **Activities** (top row) — Big things the user does. These are your backbone. They read
  left to right like a narrative: "First the user does this, then this, then this."
- **User Tasks** (second row) — Smaller steps within each activity. Still user-facing, still
  in the user's language.

### Vertical: Priority (Walking Skeleton to Nice-to-Have)

Under each user task, stories stack vertically by priority:

```
                    Search by name
                    ─────────────────
  Must have    →    Basic text search
  Should have  →    Search suggestions
  Nice to have →    Fuzzy matching
                    Search history
```

Stories near the top are essential. Stories further down are refinements, enhancements, or
edge cases.

## The Walking Skeleton

Draw a horizontal line across the map. Everything above the line is your first release —
the thinnest possible end-to-end slice that lets a user complete the whole journey, even
if each step is bare-bones.

This is the walking skeleton: it walks (works end-to-end) but it's skeletal (minimal
functionality at each step).

**Why this matters for coaching:** Teams often want to build one feature completely before
moving to the next. The walking skeleton flips this — build every feature a little bit
first, so you have something usable and testable from day one.

## Running a Story Mapping Workshop

### Before the Workshop

- Identify the target users/personas
- Have a rough product vision or problem statement
- Invite: PO, developers, UX, and anyone who understands the users
- Materials: wide wall or digital whiteboard, sticky notes, markers

### The Flow

1. **Frame the problem** (10 min) — What are we building and for whom? What problem does
   it solve?

2. **Map the backbone** (20-30 min) — Walk through the user's journey at the activity
   level. Left to right, big steps. Don't go deep yet. Ask: "What does the user do first?
   Then what? Then what?"

3. **Fill in user tasks** (20-30 min) — Under each activity, what are the specific things
   the user does? Keep it in the user's language, not technical language.

4. **Add stories under tasks** (30-45 min) — Now go deeper. What are the different ways
   each task could work? What are the variations, edge cases, and enhancements? Stack them
   vertically with the most essential on top.

5. **Slice releases** (20-30 min) — Draw horizontal lines to define releases. The first
   release is the walking skeleton. Each subsequent release adds a layer of capability.

### Facilitation Tips

- Keep the user's voice dominant: "The user searches for..." not "The system displays..."
- If debates go long, capture both options as stories and move on — prioritization will
  sort it out
- It's OK to discover gaps. That's the point. "Wait, what happens if the payment fails?"
  is a great moment in a mapping session.
- The map is never "done" — it evolves as understanding grows

## Using the Map After the Workshop

- **Sprint planning** — Pull from the top of the current release slice
- **Backlog refinement** — Use the map to see what's coming and refine stories before they
  reach the top
- **Stakeholder communication** — The map is a visual roadmap that non-technical people
  can read
- **Gap analysis** — Scan horizontally: is there a part of the user's journey with no
  stories? That might be a blind spot.

## Common Story Mapping Mistakes

- **Going too deep too early** — Spending 2 hours detailing one activity while ignoring
  the rest of the journey. Map wide first, then deep.
- **Technical language in the backbone** — "Configure database" is not a user activity.
  Keep the backbone in user terms.
- **No walking skeleton** — Building the map but never slicing it. The release slicing is
  where the real planning value lives.
- **Treating it as a one-time event** — The map should live on a wall (or digital board)
  and evolve. It's not a deliverable to file away.
