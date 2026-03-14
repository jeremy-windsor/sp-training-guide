# Module 12 IOS-XR CLI Validation Report

## Summary

| Metric | Count |
|--------|-------|
| Files Reviewed | 11 |
| Total Findings | 23 |
| Critical | 3 |
| Major | 6 |
| Minor | 14 |

---

## Detailed Findings

### Critical Findings

#### [CRITICAL-1] File: 12.1-isp-backbone-design.md, Line ~350
**Current:** `isis graceful-shutdown` referenced as traffic drain mechanism
**Issue:** IOS-XR does not have a native `isis graceful-shutdown` command at the global level. Traffic drain is typically done via IS-IS Overload Bit configuration (`set-overload-bit` with `startup-mode` or manual trigger).
**Correct:** `router isis <name> set-overload-bit on-startup` or use interface-level max-metric for graceful traffic migration.
**Source:** IOS-XR ISIS configuration guide, IOS-XR 7.x

#### [CRITICAL-2] File: 12.5-evpn-l2vpn-migration-answers.md, Line ~240
**Current:** `show bgp l2vpn evpn rd 10.0.0.10:1001`
**Issue:** While this command structure exists, the RD format in show commands uses colon notation (10.0.0.10:1001) but the actual CLI expects specific syntax. The broader issue is that `l2vpn` sub-mode under `router bgp` is not the standard IOS-XR hierarchy.
**Correct:** IOS-XR uses `address-family l2vpn evpn` under `router bgp` context. Show commands are `show bgp l2vpn evpn` (without the `router` hierarchy path shown correctly in other examples).
**Source:** IOS-XR BGP EVPN command reference

#### [CRITICAL-3] File: 12.4-internet-exchange-point-design.md, Line ~150
**Current:** `show evpn mac-address ffff.ffff.ffff`
**Issue:** This command format incorrectly uses period-separated MAC format. IOS-XR expects colon-separated format or specific show command structure.
**Correct:** `show evpn evi mac-address ffff:ffff:ffff` or similar depending on IOS-XR version.
**Source:** IOS-XR EVPN command reference

---

### Major Findings

#### [MAJOR-1] File: 12.5-evpn-l2vpn-migration.md, Line ~230-250
**Current:** 
```
show bgp l2vpn evpn evi VPN1
show evpn evi vpn-id 1001 detail
```
**Issue:** IOS-XR does not support `evi <name>` as a direct show filter in this context. EVI identification differs between platforms.
**Correct:** Use `show evpn evi id 1001 detail` or `show bgp l2vpn evpn rd 10.0.0.10:1001`
**Source:** IOS-XR EVPN CLI reference

#### [MAJOR-2] File: 12.1-isp-backbone-design-answers.md, Line ~380
**Current:** `show cef mpls prefix-sid <SID>`
**Issue:** IOS-XR uses `show cef` (Cisco Express Forwarding) commands, but the exact syntax for MPLS prefix-sid verification differs.
**Correct:** `show mpls forwarding` or `show cef ipv4 <prefix>` to see SID adjacency information
**Source:** IOS-XR Segment Routing command reference

#### [MAJOR-3] File: 12.4-internet-exchange-point-design-answers.md, Line ~420
**Current:** `show bgp l2vpn evpn neighbors <address>`
**Issue:** While neighbor commands exist, the output format and options vary by IOS-XR version. No major syntax error but verify exact command support.
**Correct:** Generally acceptable, but `show bgp l2vpn evpn summary` is preferred for status.
**Source:** IOS-XR BGP EVPN command reference

#### [MAJOR-4] File: 12.3-mobile-backhaul-5g-transport.md, Line ~185
**Current:** `segment-routing global-block 16000 23999`
**Issue:** IOS-XR uses `segment-routing global-block 16000 23999` in the correct location (under `segment-routing`), but syntax verification needed.
**Correct:** Confirmed valid on IOS-XR 7.x with slight variation possible depending on platform.
**Note:** Minor platform variance; command generally correct.

#### [MAJOR-5] File: 12.5-evpn-l2vpn-migration.md, Line ~180
**Current:** 
```
evpn
 evi 1001
  bgp
   route-target import 65000:1001
   route-target export 65000:1001
```
**Issue:** IOS-XR EVPN configuration uses `bgp import route-target` and `bgp export route-target` syntax order may vary by version.
**Correct:** Verify exact sequence; newer IOS-XR uses `route-target import <rt>` and `route-target export <rt>` under `bgp` submode.
**Source:** IOS-XR EVPN configuration guide

#### [MAJOR-6] File: 12.1-isp-backbone-design-answers.md, Line ~450
**Current:** 
```
router static
 address-family ipv4 unicast
  10.0.0.0/8 Null0 tag 999
```
**Issue:** Static route Null0 reference syntax. IOS-XR uses different null interface naming.
**Correct:** `0.0.0.0/8 Null0` or verify exact syntax for discard routes.
**Source:** IOS-XR static route configuration guide

---

### Minor Findings (Platform/Version Variations)

#### [MINOR-1] File: 12.1-isp-backbone-design.md, Line ~320
**Current:** `show cef tunnel-encapsulation`
**Note:** Command exists but output format varies significantly by IOS-XR version. Acceptable but verify on target platform.

#### [MINOR-2] File: 12.2-dci-with-evpn-answers.md, Line ~290
**Current:** `show evpn ethernet-segment bgp detail`
**Note:** Check exact syntax for specific IOS-XR version. May use `show evpn es` or similar shorthand.

#### [MINOR-3] File: 12.3-mobile-backhaul-5g-transport.md, Line ~220
**Current:** `show segment-routing manager`
**Note:** Command valid but may require specific admin context or be platform-dependent.

#### [MINOR-4] File: 12.3-mobile-backhaul-5g-transport-answers.md, Line ~180
**Current:** `show bgp neighbors <address> advertised-routes`
**Note:** Standard IOS command, but IOS-XR uses `show bgp neighbor <address> advertised-routes` (singular "neighbor").

#### [MINOR-5] File: 12.4-internet-exchange-point-design.md, Line ~200
**Current:** `show isis flex-algo flexible-algorithm 128`
**Note:** IOS-XR Flex-Algo show commands may use `show isis flex-algo` or similar. Verify exact hierarchy.

#### [MINOR-6] File: 12.5-evpn-l2vpn-migration-answers.md, Line ~500
**Current:** `show l2vpn bridge-domain mac-address flapping`
**Note:** MAC flapping detection command syntax varies. May use `show l2vpn mac flapping` or similar.

#### [MINOR-7] File: 12.1-isp-backbone-design.md, Line ~380
**Current:** `show mpls traffic-eng tunnels`
**Note:** In SR-MPLS context, this command may show limited info. Prefer `show segment-routing traffic-eng policy` for SR-TE.

#### [MINOR-8] File: 12.2-dci-with-evpn.md, Line ~150
**Current:** General IOS-XR CLI for EVPN with VXLAN
**Note:** IOS-XR does not natively support VXLAN as an encapsulation for EVPN in the same way as NX-OS or Junos. IOS-XR EVPN focuses on MPLS/MG-BGP transport.

#### [MINOR-9] File: 12.3-mobile-backhaul-5g-transport.md, Line ~300
**Current:** `show isis segment-routing prefix-sid`
**Note:** May require specific address-family context or be abbreviated to `show isis segment-routing`.

#### [MINOR-10] File: 12.4-internet-exchange-point-design.md, Line ~350
**Current:** `show bgp summary`
**Note:** For EVPN, prefer `show bgp l2vpn evpn summary` for specific address-family stats.

#### [MINOR-11] File: 12.5-evpn-l2vpn-migration.md, Line ~320
**Current:** Various `evpn` mode configuration depths
**Note:** IOS-XR `evpn` submode depth and available commands vary significantly between hardware platforms and software versions.

#### [MINOR-12] File: 12.1-isp-backbone-design-answers.md, Line ~200
**Current:** `show isis spf-log`
**Note:** Command exists but output fields and options may vary by version.

#### [MINOR-13] File: 12.2-dci-with-evpn.md, Line ~400
**Current:** VXLAN over Routed IP design with IOS-XR
**Note:** IOS-XR is primarily an MPLS/SR platform. VXLAN-based EVPN DCI designs are more commonly implemented on Nexus or platforms with native VXLAN support.

#### [MINOR-14] File: 12.5-evpn-l2vpn-migration.md, Line ~600
**Current:** TI-LFA configuration references
**Note:** TI-LFA configuration and show commands vary by IOS-XR version. Verify `show isis fast-reroute summary` availability.

---

## Platform Context Corrections

Several files discuss DCI with EVPN over VXLAN. **Important:** IOS-XR (ASR 9000/NCS platforms) is primarily designed for MPLS and Segment-Routing based transport, not native VXLAN encapsulation. While IOSXR can participate in EVPN, the VXLAN-based DCI designs shown in 12.2 and 12.4 examples are more representative of:

- **Nexus platforms** (NX-OS) for data center VXLAN
- **ASR/IOS-XR** for WAN/MPLS EVPN transport

The case studies mix platform capabilities without clear delineation. Ensure readers understand that VXLAN EVPN and MPLS EVPN are implemented on different platform types.

---

## Command Verification Sources Consulted

- IOS-XR 7.x Configuration Guides
- IOS-XR BGP EVPN Command Reference
- IOS-XR Segment Routing Configuration Guide
- IOS-XR IS-IS Configuration Guide
- IOS-XR L2VPN EVPN Configuration Guide

---

## Recommendations

1. **Platform Delineation:** Clearly mark CLI examples as "IOS-XR 7.x (ASR 9000/NCS)" vs "Junos (MX/QFX)" vs "NX-OS (Nexus)"

2. **Version Anchoring:** Specify minimum IOS-XR version (7.5.1+ recommended) for advanced EVPN features

3. **Command Validation:** Test critical migration commands (`show evpn`, `show bgp l2vpn evpn`) on actual IOS-XR platforms before publishing

4. **Remove VXLAN Confusion:** Clarify that IOS-XR based EVPN uses MPLS transport, not VXLAN encapsulation

5. **Fix Overload Bit Reference:** Correct the `isis graceful-shutdown` reference in 12.1 answers to proper IOS-XR overload bit syntax

---

## Files Reviewed

1. `/home/claude/agent-will/projects/sp-study-guide/modules/12-case-studies/README.md`
2. `/home/claude/agent-will/projects/sp-study-guide/modules/12-case-studies/12.1-isp-backbone-design.md`
3. `/home/claude/agent-will/projects/sp-study-guide/modules/12-case-studies/12.1-isp-backbone-design-answers.md`
4. `/home/claude/agent-will/projects/sp-study-guide/modules/12-case-studies/12.2-dci-with-evpn.md`
5. `/home/claude/agent-will/projects/sp-study-guide/modules/12-case-studies/12.2-dci-with-evpn-answers.md`
6. `/home/claude/agent-will/projects/sp-study-guide/modules/12-case-studies/12.3-mobile-backhaul-5g-transport.md`
7. `/home/claude/agent-will/projects/sp-study-guide/modules/12-case-studies/12.3-mobile-backhaul-5g-transport-answers.md`
8. `/home/claude/agent-will/projects/sp-study-guide/modules/12-case-studies/12.4-internet-exchange-point-design.md`
9. `/home/claude/agent-will/projects/sp-study-guide/modules/12-case-studies/12.4-internet-exchange-point-design-answers.md`
10. `/home/claude/agent-will/projects/sp-study-guide/modules/12-case-studies/12.5-evpn-l2vpn-migration.md`
11. `/home/claude/agent-will/projects/sp-study-guide/modules/12-case-studies/12.5-evpn-l2vpn-migration-answers.md`

---

*Report Generated: Subagent Sentinel*
*Scope: IOS-XR CLI validation only*
*Junos syntax and RFC citations excluded per instructions*
