# Module 08 IOS-XR CLI Validation Report

## Summary
- Files reviewed: 14
- Total findings: 6
- Critical: 4
- Minor: 2

## Detailed Findings
- Severity: critical
- File: `/home/claude/agent-will/projects/sp-study-guide/modules/08-l2vpn-evpn/8.3-evpn-mpls-vs-vxlan-answers.md`
- Line: 43-45
- Current text:
  ```cisco
  segment-routing
   vxlan
    vni 10100
  ```
- Correct text:
  ```cisco
  ! Do not configure VXLAN VNI under evpn evi via segment-routing hierarchy
  ! Keep EVPN RTs under evpn evi bgp, and map VNI in L2VPN/NVE context.
  l2vpn
   bridge group CLOUD
    bridge-domain CUSTOMER-1
     evi 100
     vni 10100
  ```
- Source: Cisco IOS XR EVPN Command Reference (EVPN commands): `evpn` hierarchy exposes `bgp|evi|interface|timers`; no `segment-routing` submode under `evpn evi`.
  https://www.cisco.com/c/en/us/td/docs/routers/asr9000/software/lxvpn/command/reference/b-lxvpn-cr-asr9000/EVPN-commands.html

- Severity: critical
- File: `/home/claude/agent-will/projects/sp-study-guide/modules/08-l2vpn-evpn/8.4-evpn-multi-homing-answers.md`
- Line: 53-55
- Current text:
  ```cisco
  interface Bundle-Ether1
   ethernet-segment
    identifier type 0 00.00.00.00.00.00.00.00.01.01
  ```
- Correct text:
  ```cisco
  evpn
   interface Bundle-Ether1
    ethernet-segment
     identifier type 0 00.00.00.00.00.00.00.00.01.01
  ```
- Source: Cisco IOS XR EVPN Command Reference shows `ethernet-segment` is entered from EVPN interface config mode (`evpn -> interface bundle-ether -> ethernet-segment`).
  https://www.cisco.com/c/en/us/td/docs/routers/asr9000/software/lxvpn/command/reference/b-lxvpn-cr-asr9000/EVPN-commands.html

- Severity: critical
- File: `/home/claude/agent-will/projects/sp-study-guide/modules/08-l2vpn-evpn/8.4-evpn-multi-homing-answers.md`
- Line: 56
- Current text:
  ```cisco
  bgp route-target import 00.00.00.00.00.00.00.00.01.01
  ```
- Correct text:
  ```cisco
  ! Remove this line as written.
  ! ES context does not use import/export keyword here; ES-Import RT is derived/handled as EVPN ES RT logic.
  ```
- Source: Cisco IOS XR EVPN command behavior for ES/RT usage (ES config under EVPN interface; ES RT handling is not configured with `import` keyword in this hierarchy).
  https://www.cisco.com/c/en/us/td/docs/routers/asr9000/software/lxvpn/command/reference/b-lxvpn-cr-asr9000/EVPN-commands.html

- Severity: minor
- File: `/home/claude/agent-will/projects/sp-study-guide/modules/08-l2vpn-evpn/8.4-evpn-multi-homing.md`
- Line: 539
- Current text:
  ```markdown
  | MH mode | single-active | single-active | **all-active** (unless CE can't do LACP) | Full bandwidth utilization |
  ```
- Correct text:
  ```markdown
  | MH mode | all-active (A/A per-flow or per-service default on IOS-XR EVPN ES) | single-active | **all-active** (unless CE can't do LACP) | Full bandwidth utilization |
  ```
- Source: Cisco IOS XR EVPN command reference sample output for `show evpn ethernet-segment detail` shows `Configured : A/A per flow (default)` / `A/A per service (default)`.
  https://www.cisco.com/c/en/us/td/docs/routers/asr9000/software/lxvpn/command/reference/b-lxvpn-cr-asr9000/EVPN-commands.html

- Severity: minor
- File: `/home/claude/agent-will/projects/sp-study-guide/modules/08-l2vpn-evpn/8.4-evpn-multi-homing.md`
- Line: 628
- Current text:
  ```markdown
  ... (Junos: explicit config; IOS-XR: auto from ESI)
  ```
- Correct text:
  ```markdown
  ... (Junos: explicit config; IOS-XR: configure matching LACP system MAC/admin-key on both PEs)
  ```
- Source: Same module already states IOS-XR requires explicit `lacp system mac` (line 532), and Cisco Link Bundling command reference shows `lacp system mac` under `interface Bundle-Ether` configuration.
  https://www.cisco.com/c/en/us/td/docs/iosxr/ncs5500/interfaces/b-ncs5500-interfaces-cli-reference/b-ncs5500-interfaces-cli-reference_chapter_011.html

- Severity: critical
- File: `/home/claude/agent-will/projects/sp-study-guide/modules/08-l2vpn-evpn/8.5-evpn-dci.md`
- Line: 543
- Current text:
  ```cisco
  evpn
   interface Bundle-Ether1
    ethernet-segment
     ...
    lacp system mac 0011.2233.4455
  ```
- Correct text:
  ```cisco
  interface Bundle-Ether1
   lacp system mac 0011.2233.4455
  !
  evpn
   interface Bundle-Ether1
    ethernet-segment
     ...
  ```
- Source: Cisco Link Bundling command reference places `lacp system mac` in interface config mode (`interface Bundle-Ether ...`).
  https://www.cisco.com/c/en/us/td/docs/iosxr/ncs5500/interfaces/b-ncs5500-interfaces-cli-reference/b-ncs5500-interfaces-cli-reference_chapter_011.html
