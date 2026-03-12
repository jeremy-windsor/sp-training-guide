# Accuracy Review Plan — SP Study Guide

> Spawn Forge (GPT-5.4, xhigh thinking, 15-min timeout) to review every section across Modules 2-12 for accuracy. Covers both design/deployment files AND theory files.

## Goal

Systematic accuracy review of all study guide content. Document any factual errors, outdated RFC references, incorrect protocol mechanics, or misleading explanations. Output a change log so we can fix markdown and regenerate TTS only for affected files.

## Execution

- **Agent**: Forge (GPT-5.4)
- **Thinking**: xhigh
- **Timeout**: 15 minutes per spawn
- **Scope**: Each spawn reviews one module (all section files within it)
- **Output**: Per-module accuracy report saved to `plans/reviews/module-XX-review.md`

## Review Checklist (per file)

For each `.md` file (design + theory + answers):
1. **RFC accuracy** — Are RFC numbers, years, and titles correct?
2. **Protocol mechanics** — Are state machines, packet formats, algorithms described correctly?
3. **Terminology** — Correct use of protocol-specific terms?
4. **Cross-references** — Do section references point to the right companion files?
5. **Vendor neutrality** — Theory files should not contain vendor-specific config (design files can)
6. **Completeness** — Any obvious omissions for IE-level depth?
7. **Consistency** — Do theory and design files agree on the same protocol details?

## Review Output Format

Each review file should contain:
```markdown
# Module X — Accuracy Review

## Summary
- Files reviewed: N
- Issues found: N (critical: N, minor: N)
- Files needing TTS regeneration: [list]

## Issues

### [filename.md] — Issue Title
- **Severity**: critical | minor | cosmetic
- **Location**: Section/heading where the issue is
- **Current text**: "what it says now"
- **Correction**: "what it should say"
- **Source**: RFC/standard reference for the correction

### [filename.md] — Issue Title
...
```

## Module Review Schedule

Each module = one Forge spawn. Run sequentially tonight.

| # | Module | Files | Issues | Critical | Fixes Commit | TTS Commit | Status |
|---|--------|-------|--------|----------|-------------|------------|--------|
| 1 | Module 2: IGP | 10 | 13 | 2 | `0663677` | `9d63307` | ✅ Done |
| 2 | Module 3: BGP | 12 | 16 | 4 | `cc9d268` | `3e2025d` | ✅ Done |
| 3 | Module 4: MPLS | 12 | 16 | 8 | `863d18d` | `76f6cad` | ✅ Done |
| 4 | Module 5: TE | 9 | 11 | 3 | `2b0e718` | `8bea47c` | ✅ Done |
| 5 | Module 6: SR | 15 | 24 | 12 | `f13b9df` | `93baa1f` | ✅ Done |
| 6 | Module 7: L3VPN | 15 | 10 | 4 | `1784fab` | `b65b1f7` | ✅ Done |
| 7 | Module 8: L2VPN/EVPN | 13 | 14 | 6 | `22f3557` | `572b594` | ✅ Done |
| 8 | Module 9: Transport | 13 | 13 | 8 | `0c0ea7b` | `5c36560` | ✅ Done |
| 9 | Module 10: Slicing | 7 | 10 | 2 | `0cdbc5a` | `f9bb347` | ✅ Done |
| 10 | Module 11: Automation | 10 | 11 | 2 | `4f58695` | `708b4be` | ✅ Done |
| 11 | Module 12: Case Studies | ~8 | — | — | — | — | ⏳ Waiting (Forge credits) |

## Totals (Modules 2-11)

| Metric | Count |
|--------|-------|
| **Total issues found** | 138 |
| **Critical** | 51 |
| **Minor** | 82 |
| **Cosmetic** | 5 |
| **Files modified** | 70+ |
| **TTS files regenerated** | 60+ |
| **Review reports** | `plans/reviews/module-{02..11}-review.md` |

## Heaviest Modules
1. **Module 6 (SR)** — 24 issues, 12 critical (SRGB, PCEP, SRv6 naming throughout)
2. **Module 4 (MPLS)** — 16 issues, 8 critical (LDP roles, FEC types, RSVP-TE priority)
3. **Module 3 (BGP)** — 16 issues, 4 critical
4. **Module 8 (L2VPN/EVPN)** — 14 issues, 6 critical (RT-1 per-ES/per-EVI role reversal)
5. **Module 9 (Transport)** — 13 issues, 8 critical (OSNR formula, 400ZR cFEC/reach)

## Forge Behavior Notes
- GPT-5.4 with 15-min timeout tends to answer questions from content instead of reviewing
- Module 9: failed once (answered questions), succeeded on v2
- Module 10: failed twice (answered questions), third attempt wrote file before timing out
- Module 11: failed once (read files without writing), succeeded on v2 with "write immediately" prompt
- Best prompt pattern: explicit "YOU ARE A REVIEWER", "DO NOT answer questions", "write findings IMMEDIATELY"

## Remaining Work

1. **Module 12 review** — waiting for Forge credits to reset
2. After Module 12: commit review reports to repo
3. Update `plans/theory-expansion.md` completion status

---

*Created: 2026-03-11*
*Last updated: 2026-03-12 07:20 MST*
*Status: 10/11 modules complete — Module 12 pending Forge credits*
