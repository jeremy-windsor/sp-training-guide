# Module 06 IOS-XR CLI Syntax Review

## Summary
Reviewed all Markdown files under `/home/claude/agent-will/projects/sp-study-guide/modules/06-sr/` (18 files total) with IOS-XR-only syntax validation focus.

Found **6 IOS-XR syntax/CLI issues**:
- **4 critical** (would fail commit or use invalid hierarchy/keywords)
- **2 minor** (invalid/incorrect operational command syntax)

---

### [6.1-sr-mpls-fundamentals-answers.md] Line 52 (Question 3) — Explicit-Null configured in invalid IOS-XR hierarchy
- **Severity**: critical
- **Current text**: "segment-routing mpls / prefix-sid-map / address-family ipv4 / explicit-null"
- **Correction**: "Configure explicit-null on the Prefix-SID itself under the IGP interface context, e.g. `router isis CORE` → `interface Loopback0` → `address-family ipv4 unicast` → `prefix-sid index <N> explicit-null`"
- **Source**: Cisco IOS-XR Segment Routing command reference (`prefix-sid ... explicit-null` under IS-IS/OSPF SR Prefix-SID configuration)

### [6.2-sr-te-policies-answers.md] Lines 92–96 (Question 2) — Wrong PCEP hierarchy (`pce/peer`) for IOS-XR SR-TE
- **Severity**: critical
- **Current text**: "segment-routing traffic-eng / pce / peer ipv4 10.0.0.100"
- **Correction**: "Use PCC hierarchy and PCE address syntax, e.g. `segment-routing` → `traffic-eng` → `pcc` → `pce address ipv4 10.0.0.100` (and precedence under each PCE address)"
- **Source**: Cisco IOS-XR Segment Routing Traffic Engineering command reference (`pcc pce address ipv4 ... precedence ...`)

### [6.4-srv6-fundamentals.md] Lines 285–292 (END.DT4 SID for L3VPN section) — SRv6 VPN config placed under `vrf` instead of BGP VRF AF
- **Severity**: critical
- **Current text**: "vrf cust-a / address-family ipv4 unicast / segment-routing srv6 / locator MAIN / alloc mode per-vrf"
- **Correction**: "Place SRv6 VPN SID allocation under BGP VRF address-family, e.g. `router bgp <asn>` → `vrf cust-a` → `address-family ipv4 unicast` → `segment-routing srv6` → `locator MAIN` → `alloc mode per-vrf`"
- **Source**: Cisco IOS-XR SRv6 L3VPN configuration guide / command reference (BGP VRF AF SRv6 service SID allocation)

### [6.4-srv6-fundamentals.md] Lines 307 and 667 (SRv6 policy examples) — `end-point` missing address-family keyword
- **Severity**: critical
- **Current text**: "color 100 end-point fc00:0:7::1" and "color 200 end-point fc00:0:7::1"
- **Correction**: "Use `end-point ipv6 <address>`, e.g. `color 100 end-point ipv6 fc00:0:7::1`"
- **Source**: Cisco IOS-XR SR-TE command reference (`color <id> end-point ipv4|ipv6 <addr>`)

### [6.4-srv6-fundamentals.md] Line 444 (Troubleshooting table) — Invalid IOS-XR corrective command for END.DT4 binding
- **Severity**: critical
- **Current text**: "Configure `vrf <name> segment-routing srv6 locator <loc> alloc mode per-vrf`"
- **Correction**: "Configure under BGP VRF address-family: `router bgp <asn>` → `vrf <name>` → `address-family ipv4 unicast` → `segment-routing srv6` → `locator <loc>` → `alloc mode per-vrf`"
- **Source**: Cisco IOS-XR SRv6 L3VPN command reference

### [6.6-sr-migration-strategies.md] Line 723 (Common Issues table) — Invalid IOS-XR operational command
- **Severity**: minor
- **Current text**: "show ipv6 segment-routing"
- **Correction**: "Use IOS-XR SRv6 operational commands such as `show segment-routing srv6 sid` and/or `show segment-routing srv6 locator`"
- **Source**: Cisco IOS-XR Segment Routing / SRv6 command reference
