# Section Templates

Two templates: **Design** (existing sections) and **Theory** (protocol mechanics).

## Design Template

Use this for design/deployment sections (e.g., `2.1-isis-deep-dive.md`).

---

```markdown
# {Module}.{Section} — {Title}

## Overview
> One-paragraph summary. Why does this matter in an SP network?

## Prerequisites
- List prior sections/knowledge needed

## Theory

### Concepts
- Core protocol/feature mechanics
- Packet/frame formats where relevant
- Control plane vs data plane behavior

### Architecture
- Where this fits in the SP topology
- Scale considerations
- Failure domains and blast radius

### Design Considerations
- When to use (and when NOT to)
- Trade-offs and gotchas
- Vendor differences worth noting

## Configuration

### IOS-XR
```cisco
! Annotated config snippet
```

### Junos
```junos
# Annotated config snippet
```

### Nokia SR-OS (optional)
```nokia
# Annotated config snippet
```

### Key Knobs
| Parameter | Default | Recommended | Why |
|-----------|---------|-------------|-----|
| example   | value   | value       | reason |

## Verification & Monitoring

### Show Commands
| Command (IOS-XR) | Command (Junos) | What It Shows |
|-------------------|-----------------|---------------|
| `show ...`        | `show ...`      | description   |

### What Good Looks Like
- Expected states and outputs
- Key fields to check

### Telemetry Paths
- YANG model paths for streaming telemetry (if applicable)

## Troubleshooting

### Common Issues
| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| symptom | cause       | fix |

### Methodology
1. Step-by-step triage approach
2. Tools and commands in order
3. Escalation criteria

### War Stories
> Real-world scenario illustrating a non-obvious failure mode.

## Lab Exercise
- **Topology**: Reference to lab file in `labs/`
- **Objective**: What the student should achieve
- **Validation**: How to confirm success
- **Stretch Goal**: Advanced variation

## Quick Reference
- Key RFCs: RFC XXXX
- Key YANG models: `model-name`
- Cert relevance: IE-SP objective mapping

## Review Questions
1. Scenario-based question
2. Design decision question
3. Troubleshooting question

---
*Sources: [list references used]*
```

---

## Theory Template

Use this for protocol theory sections (e.g., `2.1-isis-deep-dive-theory.md`).
See `plans/theory-expansion.md` for the full plan, rules, and checklist.

```markdown
# {Module}.{Section} — {Title} — Protocol Theory

## Protocol Overview
- What problem it solves
- Where it sits in the stack (L2/L3/control plane/data plane)
- Historical context (when created, why, what it replaced)

## Core Mechanisms

### [Mechanism 1: e.g., Adjacency Formation]
- State machine / FSM with state descriptions
- Packet/PDU format (field-by-field breakdown)
- Timers and their defaults (with rationale)

### [Mechanism 2: e.g., Link-State Database]
- Data structures
- Flooding/synchronization algorithms
- Consistency checks

### [Mechanism 3: e.g., SPF Computation]
- Algorithm description (Dijkstra, Bellman-Ford, etc.)
- Complexity and scaling behavior
- Incremental vs full computation

## Key RFCs & Standards
| RFC | Title | What It Defines |
|-----|-------|----------------|
| RFC XXXX | Title | Brief description |

## Protocol Interactions
- How it interacts with other protocols in the guide
- Dependencies and assumptions
- Cross-reference to design file: `→ See X.Y-section-name.md`

## Edge Cases & Gotchas
- Known implementation differences between vendors
- Common misunderstandings
- What the RFC says vs what vendors actually do

## Further Reading
- Definitive books, papers, conference talks

---
*This is a theory companion to [X.Y — Title](X.Y-section-name.md).*
*For deployment, configuration, and troubleshooting, see the design file.*
```
