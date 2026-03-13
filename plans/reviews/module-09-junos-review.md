# Module 09 Junos CLI Validation Report

## Summary
- Files reviewed: 14
- Total findings: 11
- Critical: 10
- Minor: 1

## Detailed Findings

- Severity: critical
- File: `/home/claude/agent-will/projects/sp-study-guide/modules/09-transport/9.2-dwdm-fundamentals.md`
- Line: 443
- Current text: `set interfaces et-0/0/0 otn-options performance-monitoring enable`
- Correct text: Use documented OTN hierarchy only (for example, `set interfaces et-0/0/0 otn-options ...` with valid substatements such as `fec`, `tti`, `trigger`, `odu-signal-degrade`). If PM is intended, use transport PM operational commands (for example, `show interfaces transport pm ...`) rather than a non-existent `performance-monitoring enable` knob under `otn-options`.
- Source: Juniper CLI reference, `otn-options` syntax (no `performance-monitoring` substatement): https://www.juniper.net/documentation/en_US/junos12.3/topics/reference/configuration-statement/otn-options-edit-interfaces.html

- Severity: critical
- File: `/home/claude/agent-will/projects/sp-study-guide/modules/09-transport/9.2-dwdm-fundamentals.md`
- Line: 446
- Current text: `show interfaces et-0/0/0 optics-diagnostics`
- Correct text: `show interfaces diagnostics optics et-0/0/0`
- Source: Juniper command syntax: `show interfaces diagnostics optics interface-name` — https://www.juniper.net/documentation/en_US/junos12.2/topics/reference/command-summary/show-interfaces-diagnostics-optics-ex-series.html

- Severity: critical
- File: `/home/claude/agent-will/projects/sp-study-guide/modules/09-transport/9.3-otn-optical-transport-network.md`
- Line: 445
- Current text: `set interfaces et-0/0/0 otn-options wavelength-channel frequency 193100`
- Correct text: Do not use `wavelength-channel` under `otn-options`. Use documented `otn-options` substatements; if optical wavelength tuning is intended, use the interface `optics-options` hierarchy for tunable optics.
- Source: Juniper CLI references: `otn-options` syntax (no `wavelength-channel`) — https://www.juniper.net/documentation/en_US/junos12.3/topics/reference/configuration-statement/otn-options-edit-interfaces.html ; `optics-options` hierarchy under interfaces — https://www.juniper.net/documentation/en_US/junos13.2/topics/reference/configuration-statement/optics-options-edit-interfaces.html

- Severity: critical
- File: `/home/claude/agent-will/projects/sp-study-guide/modules/09-transport/9.3-otn-optical-transport-network.md`
- Line: 448
- Current text: `set interfaces et-0/0/0 otn-options otu-options ...` (and related `odu-options` hierarchy through lines 493)
- Correct text: Replace non-existent `otu-options` / `odu-options` nested hierarchy with valid `otn-options` statements (`fec`, `tti`, `trigger`, `odu-signal-degrade`, etc.) supported by Junos at `[edit interfaces <ifd> otn-options]`.
- Source: Juniper `otn-options` syntax and hierarchy — https://www.juniper.net/documentation/en_US/junos12.3/topics/reference/configuration-statement/otn-options-edit-interfaces.html

- Severity: critical
- File: `/home/claude/agent-will/projects/sp-study-guide/modules/09-transport/9.3-otn-optical-transport-network.md`
- Line: 542
- Current text: `show interfaces et-0/0/0 otn-otu` (and related `otn-odu`/`show protocols otn-topology ...` rows through line 551)
- Correct text: Use supported Junos OTN/optics operational syntax (for example, `show interfaces transport pm otn ...` for PM and `show interfaces diagnostics optics <if>` for optics DOM), not `show interfaces <if> otn-otu/otn-odu`.
- Source: Juniper command references: `show interfaces diagnostics optics` — https://www.juniper.net/documentation/en_US/junos12.2/topics/reference/command-summary/show-interfaces-diagnostics-optics-ex-series.html ; `show interfaces transport pm` — https://www.juniper.net/documentation/us/en/software/junos/cli-reference/topics/ref/command/show-interfaces-transport-pm.html

- Severity: critical
- File: `/home/claude/agent-will/projects/sp-study-guide/modules/09-transport/9.4-packet-optical-integration.md`
- Line: 615
- Current text: `interfaces { et-0/0/0 { srlg { ... } } }`
- Correct text: Define SRLG objects under `routing-options srlg ...` and apply SRLG association under supported protocol hierarchy (for example, `protocols mpls interface <if> srlg <name>`), not directly under `interfaces`.
- Source: Juniper `srlg` hierarchy levels include `[edit routing-options]` and `[edit protocols mpls interface interface-name]` — https://www.juniper.net/documentation/en_US/junos13.2/topics/reference/configuration-statement/srlg-edit-routing-options.html

- Severity: critical
- File: `/home/claude/agent-will/projects/sp-study-guide/modules/09-transport/9.4-packet-optical-integration.md`
- Line: 658
- Current text: `admin-group { exclude chicago-dallas-conduit-1; }` used as “Named SRLG exclusion”
- Correct text: Use SRLG exclusion with `exclude-srlg` in the LSP/RSVP context; do not repurpose `admin-group` as SRLG exclusion.
- Source: Juniper `exclude-srlg` statement and hierarchy — https://www.juniper.net/documentation/en_US/junos13.2/topics/reference/configuration-statement/exclude-srlg-edit-protocols-mpls.html

- Severity: critical
- File: `/home/claude/agent-will/projects/sp-study-guide/modules/09-transport/9.4-packet-optical-integration.md`
- Line: 672
- Current text: `routing-options { source-packet-routing { ... sr-policy ... } }`
- Correct text: Configure SR-TE policy objects under `protocols source-packet-routing` (for example, `segment-list` and `source-routing-path`), not under `routing-options source-packet-routing` with `sr-policy` syntax.
- Source: Juniper `source-routing-path` hierarchy at `[edit protocols source-packet-routing]` — https://www.juniper.net/documentation/us/en/software/junos/cli-reference/topics/ref/statement/autogen-protocols-source-packet-routing-source-routing-path.html

- Severity: critical
- File: `/home/claude/agent-will/projects/sp-study-guide/modules/09-transport/9.5-coherent-optics.md`
- Line: 497
- Current text: `# NOTE: optics-options lives under chassis hierarchy, NOT interfaces`
- Correct text: `optics-options` for coherent port tuning is configured under interface hierarchy (platform/release dependent options still live under `interfaces <if> optics-options`).
- Source: Juniper `optics-options` hierarchy under interfaces — https://www.juniper.net/documentation/en_US/junos13.2/topics/reference/configuration-statement/optics-options-edit-interfaces.html ; 400ZR task flow under interface hierarchy — https://www.juniper.net/documentation/us/en/software/junos/interfaces-ethernet/topics/task/configure-400zr-zrm-coherent-optics.html

- Severity: critical
- File: `/home/claude/agent-will/projects/sp-study-guide/modules/09-transport/9.5-coherent-optics.md`
- Line: 499
- Current text: `set chassis fpc 0 pic 0 optics-options wavelength 1552.52` (also lines 500, 503, 506, 527, 528)
- Correct text: Use interface hierarchy for these knobs, e.g. `set interfaces et-0/0/0 optics-options wavelength 1552.52` (and corresponding `tx-power`, `wavelength frequency`, `modulation`, `alarm` under `interfaces ... optics-options`).
- Source: Juniper `optics-options` hierarchy — https://www.juniper.net/documentation/en_US/junos13.2/topics/reference/configuration-statement/optics-options-edit-interfaces.html

- Severity: minor
- File: `/home/claude/agent-will/projects/sp-study-guide/modules/09-transport/9.5-coherent-optics.md`
- Line: 595
- Current text: `show interfaces et-0/0/0 media-type`
- Correct text: Use a supported form such as `show interfaces diagnostics optics et-0/0/0` (for optics/DSP visibility) or `show interfaces media et-0/0/0` for media detail.
- Source: Juniper `show interfaces` command family (includes `diagnostics optics` and `media` forms) — https://www.juniper.net/documentation/us/en/software/junos/cli-reference/topics/ref/command/show-interfaces-gigabit-ethernet.html
