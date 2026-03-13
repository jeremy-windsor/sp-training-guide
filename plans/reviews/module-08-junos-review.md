# Module 08 Junos CLI Validation Report

## Summary
- Files reviewed: 14
- Total findings: 7
- Critical: 3
- Minor: 4

## Detailed Findings

1) 
- Severity: minor
- File: `8.2-evpn-fundamentals.md`
- Line: 503
- Current text: ``show bridge domain CUST-A``
- Correct text: ``show bridge domain instance CUST-A`` (or ``show bridge domain BD-100 instance CUST-A``)
- Source: Junos CLI reference for `show bridge domain` (expects bridge-domain/instance context, not routing-instance name as a standalone BD token).

2)
- Severity: minor
- File: `8.3-evpn-mpls-vs-vxlan.md`
- Line: 423
- Current text: ``show bridge-domain``
- Correct text: ``show bridge domain``
- Source: Junos CLI Reference: `show bridge domain` command syntax.

3)
- Severity: minor
- File: `8.3-evpn-mpls-vs-vxlan.md`
- Line: 425
- Current text: ``show vxlan vni``
- Correct text: ``show ethernet-switching vxlan-tunnel-end-point source``
- Source: Junos CLI Reference: VXLAN operational commands are under `show ethernet-switching vxlan-tunnel-end-point ...` (not `show vxlan vni`).

4)
- Severity: minor
- File: `8.3-evpn-mpls-vs-vxlan.md`
- Line: 427
- Current text: ``show evpn vxlan-vni``
- Correct text: ``show evpn instance bridge-domains`` (or `show evpn instance <name> bridge-domains`)
- Source: Junos CLI Reference for `show evpn instance` options; no standard `show evpn vxlan-vni` command.

5)
- Severity: critical
- File: `8.4-evpn-multi-homing-answers.md`
- Line: 443
- Current text: ``fast-hello;`` (under `aggregated-ether-options { lacp { ... } }`)
- Correct text: remove `fast-hello;` and use supported LACP timer knob: ``periodic fast;``
- Source: Junos LACP hierarchy/statement reference (`lacp` under aggregated Ethernet supports `periodic fast|slow`; `fast-hello` is not a valid knob in this context).

6)
- Severity: critical
- File: `8.5-evpn-dci.md`
- Line: 728-729
- Current text: 
  - ``community SOO-SITE-A members soo:65000:100;``
  - ``community SOO-SITE-B members soo:65000:200;``
- Correct text:
  - ``community SOO-SITE-A members origin:65000:100;``
  - ``community SOO-SITE-B members origin:65000:200;``
- Source: Junos `policy-options community` extended community formats use `origin:` for Site-of-Origin (SoO), not `soo:`.

7)
- Severity: critical
- File: `8.5-evpn-dci.md`
- Line: 735, 738
- Current text:
  - ``instance-type mac-vrf;``
  - ``encapsulation mpls;``
- Correct text: for EVPN-MPLS BGW on MX, use `instance-type evpn` (or `virtual-switch` per service model) with EVPN-MPLS hierarchy; do not use `mac-vrf` for this case.
- Source: Juniper “MAC-VRF Routing Instance Type Overview” notes EVPN-MPLS with `mac-vrf` is not supported on MX platforms.
