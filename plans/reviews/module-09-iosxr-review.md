# Module 09 IOS-XR CLI Validation Report

## Summary
- Files reviewed: 14
- Total findings: 7
- Critical: 3
- Minor: 4

## Detailed Findings
- Severity: minor
- File: /home/claude/agent-will/projects/sp-study-guide/modules/09-transport/9.1-sp-transport-hierarchy.md
- Line: 424
- Current text: `2. **Check light levels** — \`show interface <x> phy\` or \`show controllers optics <x>\` (IOS-XR)`
- Correct text: `2. **Check light levels** — \`show controllers optics <r/s/i/p>\` (and, where supported, \`show controllers coherentDSP <r/s/i/p>\`)`
- Source: Cisco NCS 5500 Interface and Hardware Component Configuration Guide (IOS XR 7.9.x), “Use the show controllers optics r/s/i/p command …”; Cisco NCS 1004 Command Reference (`show controllers`, `controller optics`).

- Severity: minor
- File: /home/claude/agent-will/projects/sp-study-guide/modules/09-transport/9.1-sp-transport-hierarchy-answers.md
- Line: 54
- Current text: `Check \`show interface <x> | include CRC|errors|input\` on both ends.`
- Correct text: `Check \`show interfaces <intf> | include CRC|errors|input\` and optics/controller state with \`show controllers optics <r/s/i/p>\`.`
- Source: Cisco IOS XR command usage in platform guides/command references is `show interfaces` and `show controllers optics` (NCS 5500/NCS 1004 docs).

- Severity: critical
- File: /home/claude/agent-will/projects/sp-study-guide/modules/09-transport/9.3-otn-optical-transport-network.md
- Line: 357
- Current text: `dwdm-carrier 100MHz-grid frequency 19310  ! 193.1 THz (C-band center)`
- Correct text: `dwdm-carrier 100MHz-grid frequency 1931000  ! 193.1 THz`
- Source: Cisco NCS 1004 Command Reference, `dwdm-carrier` examples show 100MHz-grid frequency format like `1865000` (100 MHz units), not 5-digit values.

- Severity: minor
- File: /home/claude/agent-will/projects/sp-study-guide/modules/09-transport/9.5-coherent-optics.md
- Line: 437
- Current text: `! NCS 5500/5700 use 10 MHz units; Cisco 8000 uses 5-tuple interface naming.`
- Correct text: `! On IOS-XR routed optical examples, frequency values are entered using documented dwdm-carrier grid units (commonly 100MHz-grid values such as 1960625 on NCS 5500 examples). Verify exact syntax per platform release.`
- Source: Cisco NCS 5500 Interface and Hardware Component Configuration Guide (IOS XR 7.9.x) examples (e.g., frequency displayed/used in 100 MHz steps such as 1960625); Cisco NCS 1004 Command Reference (`100MHz-grid`).

- Severity: critical
- File: /home/claude/agent-will/projects/sp-study-guide/modules/09-transport/9.5-coherent-optics.md
- Line: 441
- Current text: `dwdm-carrier 75GHz-grid frequency 19310    ! 193.1 THz (frequency in 10 MHz units)`
- Correct text: `dwdm-carrier 100MHz-grid frequency 1931000    ! 193.1 THz`
- Source: Cisco command references for NCS routed-optical controllers document `dwdm-carrier` with `50GHz-grid` / `100MHz-grid` forms and 7-digit frequency values (e.g., 1865000, 1960625).

- Severity: critical
- File: /home/claude/agent-will/projects/sp-study-guide/modules/09-transport/9.5-coherent-optics.md
- Line: 447
- Current text: `dwdm-carrier flex-grid frequency 19350 slot-width 75`
- Correct text: `dwdm-carrier flex-grid frequency 1935000 slot-width 75` (or platform-equivalent syntax with the same 193.5 THz value)
- Source: IOS-XR routed optical frequency examples use values in the ~1913000–1961000 range for C-band channels (Cisco NCS 5500/NCS 1004 docs and examples), so `19350` is off by orders of magnitude.

- Severity: minor
- File: /home/claude/agent-will/projects/sp-study-guide/modules/09-transport/9.5-coherent-optics.md
- Line: 597
- Current text: `` `show controllers optics 0/0/0/0 cd-min cd-max` ``
- Correct text: `` `show controllers optics 0/0/0/0` `` (CD thresholds are configured under `controller optics ... cd-min/cd-max`; they are not appended as `show` arguments)
- Source: Cisco IOS XR optics command syntax: `cd-min`/`cd-max` are controller configuration parameters; operational view is via `show controllers optics r/s/i/p`.
