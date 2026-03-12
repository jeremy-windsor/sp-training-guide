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

| # | Module | Files to Review | Status |
|---|--------|----------------|--------|
| 1 | Module 2: IGP | 2.1-2.4 (design + theory + answers) | ⬜ |
| 2 | Module 3: BGP | 3.1-3.4 (design + theory + answers) | ⬜ |
| 3 | Module 4: MPLS | 4.1-4.4 (design + theory + answers) | ⬜ |
| 4 | Module 5: TE | 5.1-5.3 (design + theory + answers) | ⬜ |
| 5 | Module 6: SR | 6.1-6.5 (design + theory + answers) | ⬜ |
| 6 | Module 7: L3VPN | 7.1-7.5 (design + theory + answers) | ⬜ |
| 7 | Module 8: L2VPN/EVPN | 8.1-8.5 (design + theory + answers) | ⬜ |
| 8 | Module 9: Transport | 9.1-9.5 (design + theory + answers) | ⬜ |
| 9 | Module 10: Slicing | 10.1-10.3 (design + theory + answers) | ⬜ |
| 10 | Module 11: Automation | 11.1-11.5 (design + theory + answers) | ⬜ |
| 11 | Module 12: Case Studies | 12.1-12.4 (design + answers) | ⬜ |

## After Review

1. Collect all review files from `plans/reviews/`
2. Triage: fix critical issues first, then minor
3. Apply fixes to markdown files
4. Regenerate TTS ONLY for changed files
5. Commit and push

---

*Created: 2026-03-11*
*Status: Pending — ready to execute*
