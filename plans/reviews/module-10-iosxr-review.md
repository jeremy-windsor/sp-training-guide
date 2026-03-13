# Module 10 IOS-XR CLI Validation Report

## Summary
- Files reviewed: 8
- Total findings: 4
- Critical: 1
- Minor: 3

**Overall assessment:** Module 10's IOS-XR content is solid. The Flex-Algo, SR-TE ODN, VRF, BGP, PTP, and SyncE configurations are syntactically correct and follow proper IOS-XR hierarchy. The FlexE section appropriately caveats that CLI is conceptual/representative. One critical IOS/IOS-XE command misattributed to IOS-XR in the answer key, and a few minor syntax issues from IOS-XE leaking into IOS-XR examples.

---

## Detailed Findings

### Finding 1

- **Severity:** critical
- **File:** `10.3-5g-xhaul-requirements-answers.md`
- **Line:** 156
- **Current text:** `show network-clocks synchronization` (IOS-XR)
- **Correct text:** `show frequency synchronization interfaces` or `show frequency synchronization selection` (IOS-XR)
- **Source:** `show network-clocks synchronization` is an IOS/IOS-XE command (under `network-clocks` hierarchy). IOS-XR uses the `frequency synchronization` hierarchy for all SyncE operations. The correct troubleshooting commands are `show frequency synchronization interfaces` (per-interface lock state and QL), `show frequency synchronization selection` (active source selection process), and `show frequency synchronization clock-interfaces` (clock interface details). The main content file (10.3) correctly lists these commands in its verification table (lines ~395-397), so this is an answer-key-only error.

---

### Finding 2

- **Severity:** minor
- **File:** `10.1-network-slicing-concepts.md`
- **Lines:** 555, 559
- **Current text:** `random-detect dscp-based`
- **Correct text:** `random-detect` (for default WRED) or explicit per-DSCP thresholds, e.g., `random-detect dscp af31 <min> <max> <mark-probability>`
- **Source:** `random-detect dscp-based` is IOS/IOS-XE syntax that enables DSCP-based WRED as a mode selector. IOS-XR does not have this keyword. In IOS-XR, WRED is enabled with `random-detect` (which applies default parameters) or configured with explicit per-DSCP thresholds using `random-detect dscp <value> <min-threshold> <max-threshold>`. For a study guide example, `random-detect` alone is sufficient to convey the intent. If per-DSCP differentiation is desired, individual `random-detect dscp` entries are needed.

---

### Finding 3

- **Severity:** minor
- **File:** `10.1-network-slicing-concepts.md`
- **Lines:** 532–565 (QoS block)
- **Current text:** Class-maps terminated with `!` and policy-map terminated with `!`
- **Correct text:** Class-maps should use `end-class-map` and policy-map should use `end-policy-map`
- **Source:** IOS-XR `show running-config` outputs `end-class-map` as the formal class-map terminator and `end-policy-map` as the formal policy-map terminator. While `!` is commonly used as a visual separator in documentation, the 10.3 file (lines 314, 318, 333) correctly uses `end-class-map` and `end-policy-map` for the same constructs. For consistency across the module and accuracy as IOS-XR reference material, 10.1 should match. This is a style/consistency issue rather than a functional error — the configuration would still be accepted by the parser.

---

### Finding 4

- **Severity:** minor
- **File:** `10.2-flexe-flexible-ethernet-answers.md`
- **Line:** 93
- **Current text:** `show flexe group <id> calendar` (attributed to IOS-XR)
- **Correct text:** `show controllers FlexEGroup <rack/slot/instance> calendar`
- **Source:** The main 10.2 document (line 584) correctly uses `show controllers FlexEGroup 0/0/0 calendar` for IOS-XR, following the standard IOS-XR controller hierarchy for hardware features. The answer key uses a shortened `show flexe group` form that doesn't match IOS-XR command syntax. IOS-XR manages FlexE through the `controller` hierarchy, not a standalone `flexe` command tree.

---

## Items Verified Clean

The following IOS-XR constructs were reviewed and found correct:

- **Flex-Algo definitions** (10.1, 10.3): `metric-type igp|delay|te`, `affinity exclude-any` with named affinities, `advertise-definition` — all correct under `router isis`
- **Affinity-map** (10.1): `segment-routing / affinity-map / name <x> bit-position <n>` — correct hierarchy
- **Interface flex-algo affinity** (10.1): `affinity flex-algo / color <name>` under `router isis / interface` — correct
- **Performance-measurement** (10.1): `performance-measurement / interface / delay-measurement / advertise-delay` — correct hierarchy
- **Prefix-SID per algorithm** (10.1, 10.3): `prefix-sid algorithm <N> absolute <value>` under `router isis / interface Loopback0 / address-family` — correct
- **VRF configuration** (10.1, 10.3): `vrf <name> / address-family / import|export route-target` — correct
- **Extcommunity-set opaque** (10.1): color community definitions — correct RPL syntax
- **Route-policy with set extcommunity color** (10.1): correct RPL syntax
- **BGP VRF with rd auto** (10.1): correct
- **SR-TE ODN templates** (10.1): `on-demand color <N> / dynamic / sid-algorithm <N>` — correct hierarchy
- **QoS priority levels** (10.1, 10.3): `priority level 1|2` with `police rate percent` — correct for ASR 9000, platform note for NCS 5500 is accurate
- **PTP configuration** (10.3): `ptp / clock / domain / profile g.8275.1`, named profiles with `transport ethernet`, `port state slave-only`, log-interval values — all correct
- **SyncE configuration** (10.3): `frequency synchronization / quality itu-t option 1` and per-interface `frequency synchronization / selection input / priority` — correct
- **FlexE controller hierarchy** (10.2): `controller FlexEGroup`, `controller FlexEClient` with `flexe-group`, `client-id`, `calendar-slots` — reasonable conceptual model (file appropriately caveats exact syntax varies by platform)
- **All show commands in verification tables** (10.1, 10.2, 10.3 main files): correct IOS-XR command syntax
- **Telemetry sensor paths** (10.1, 10.3): `Cisco-IOS-XR-*-oper` YANG paths are plausible

---

*Reviewed: 2026-03-13 by Sentinel IOS-XR CLI Validator*
