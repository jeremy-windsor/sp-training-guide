# Module 3 (BGP) — Accuracy Review

## Summary
- Files reviewed: 12
- Issues found: 16 (critical: 4, minor: 11, cosmetic: 1)
- Files needing TTS regeneration: ["3.1-bgp-fundamentals-at-sp-scale-theory.md", "3.2-ibgp-design-theory.md", "3.2-ibgp-design.md", "3.2-ibgp-design-answers.md", "3.3-ebgp-peering.md", "3.3-ebgp-peering-answers.md", "3.4-bgp-policy-and-traffic-engineering.md"]

## Issues

### 3.1-bgp-fundamentals-at-sp-scale-theory.md — ORIGIN attribute misstates how redistributed IGP routes are marked
- **Severity**: minor
- **Location**: Path Attributes → ORIGIN (Type 1)
- **Current text**: "**IGP (0)**: Originated via network statement or redistribution from IGP. Highest preference."
- **Correction**: "**IGP (0)** should be described as locally originated into BGP (for example via the BGP `network` mechanism, or aggregate generation depending on implementation). Routes redistributed into BGP are generally marked **INCOMPLETE**, even if the source protocol was an IGP."
- **Source**: RFC 4271, Section 5.1.1

### 3.1-bgp-fundamentals-at-sp-scale-theory.md — Capability 73 is misattributed to RFC 9234
- **Severity**: minor
- **Location**: Message Type 1: OPEN → Optional Parameters → Capabilities
- **Current text**: "Capability 73: FQDN (RFC 9234 informational)"
- **Correction**: "Capability 73 is FQDN Capability in the IANA capability registry; RFC 9234 defines **BGP Role**, which is capability code 9, not FQDN."
- **Source**: IANA BGP Capability Codes registry; RFC 9234

### 3.1-bgp-fundamentals-at-sp-scale-theory.md — RFC 8203 is described as a capability when it is not
- **Severity**: minor
- **Location**: Message Type 3: NOTIFICATION
- **Current text**: "RFC 8203 added a \"Shutdown Communication\" capability: the NOTIFICATION can carry a UTF-8 text string explaining why the session was closed"
- **Correction**: "RFC 8203 did not add a BGP capability. It updates the Cease NOTIFICATION Administrative Shutdown / Administrative Reset handling so a shutdown communication string can be carried in the NOTIFICATION data."
- **Source**: RFC 8203

### 3.1-bgp-fundamentals-at-sp-scale-theory.md — MED oscillation mitigation is described incorrectly
- **Severity**: minor
- **Location**: Edge Cases & Gotchas → MED oscillation
- **Current text**: "Solution: `bgp always-compare-med` makes behavior deterministic (at the cost of sometimes suboptimal path selection), or `bgp deterministic-med` groups paths by neighbor AS before comparison."
- **Correction**: "`always-compare-med` does not make MED behavior deterministic and can contribute to the RFC 3345 oscillation problem when MED is compared across different neighboring ASes. The deterministic mitigation is to compare MED only where appropriate and/or group paths by neighboring AS before comparison (`deterministic-med` behavior)."
- **Source**: RFC 3345; RFC 4271 Section 9.1.2.2

### 3.2-ibgp-design-theory.md — ORIGINATOR_ID behavior is wrong for locally originated RR routes
- **Severity**: minor
- **Location**: Route Reflectors → Loop Prevention → ORIGINATOR_ID
- **Current text**: "If an RR originates the route itself, ORIGINATOR_ID = its own Router ID."
- **Correction**: "ORIGINATOR_ID is added by a route reflector when it reflects a route and identifies the route's originator. A locally originated route is not 'reflected' with a self ORIGINATOR_ID just because the local speaker is also an RR."
- **Source**: RFC 4456, Section 8

### 3.2-ibgp-design-theory.md — ORF section presents nonstandard community-based ORF types as if they were standard here
- **Severity**: minor
- **Location**: Outbound Route Filtering (ORF)
- **Current text**: "Community ORF: Filter based on community values. Extended Community ORF: Filter based on extended communities (useful for VPN RT-based filtering)."
- **Correction**: "The standards cited here define the ORF framework (RFC 5291) and Address Prefix ORF (RFC 5292). For VPN route-target scaling, the standardized mechanism is RT-Constrain (RFC 4684). Community/extended-community ORF should not be presented as the standard VPN scaling method in this theory file."
- **Source**: RFC 5291; RFC 5292; RFC 4684

### 3.2-ibgp-design.md — Confederations are described as inherently giving better path diversity
- **Severity**: minor
- **Location**: RR vs. Confederation Decision table
- **Current text**: "Path diversity | ADD-PATH solves it | Naturally better (eBGP behavior)"
- **Correction**: "Confederations do not inherently eliminate path hiding. Border speakers still advertise selected best paths per peer unless additional mechanisms are used. A safer wording is that confederations may change where best-path decisions occur, but they do not automatically provide full path diversity."
- **Source**: RFC 4271; RFC 5065

### 3.2-ibgp-design-answers.md — Session-count arithmetic is materially understated
- **Severity**: minor
- **Location**: Question 3 answer → "Equivalent scaling"
- **Current text**: "Total iBGP sessions: ~200 (PE→regional) + 8 (regional→top) + a few (inter-RR)."
- **Correction**: "If 200 PEs each peer with two regional RRs, PE→RR sessions are roughly **400**, not 200. With 8 regional RRs and 2 top-level RRs, regional→top sessions are typically **16** before counting any RR-to-RR redundancy sessions."
- **Source**: RFC 4456 deployment model; basic RR topology arithmetic

### 3.3-ebgp-peering.md — Claims GTSM and ebgp-multihop cannot be used together
- **Severity**: critical
- **Location**: Multihop eBGP
- **Current text**: "**Caution**: `ebgp-multihop` disables GTSM. You can't use both."
- **Correction**: "Protocol-wise, GTSM can be used with a bounded multi-hop session by validating the expected hop count; RFC 5082 even includes multi-hop guidance. If a particular vendor CLI makes `ttl-security` and `ebgp-multihop` mutually exclusive, that should be called out as a platform caveat, not a protocol rule."
- **Source**: RFC 5082 (especially Appendix A)

### 3.3-ebgp-peering.md — Example outbound policy omits self-originated routes despite earlier text saying to send own + customer routes
- **Severity**: minor
- **Location**: Configuration → Route-map `PEER-OUT`
- **Current text**: "route-map PEER-OUT permit 10 / match community CUSTOMER-ROUTES"
- **Correction**: "The outbound policy needs an explicit path for the SP's own locally originated/aggregate routes in addition to customer routes, otherwise self-originated prefixes are suppressed unless they were tagged elsewhere. This should match the earlier design rule: 'Only your own + customer prefixes.'"
- **Source**: RFC 7454 operational policy guidance; valley-free export practice

### 3.3-ebgp-peering-answers.md — GTSM vs ebgp-multihop explanation is protocol-wrong
- **Severity**: critical
- **Location**: Question 3 answer
- **Current text**: "They're mutually exclusive because they enforce opposite TTL logic."
- **Correction**: "GTSM and multi-hop peering are not inherently mutually exclusive at the protocol level. GTSM uses TTL=255 with an acceptance threshold based on expected hop count; that model can protect bounded multi-hop eBGP sessions. The answer should distinguish protocol behavior from vendor CLI limitations."
- **Source**: RFC 5082

### 3.3-ebgp-peering-answers.md — Invalid RPKI scenario is impossible as written
- **Severity**: minor
- **Location**: Question 2 answer → Scenario C
- **Current text**: "Scenario C: No ROA exists for the covering prefix, but a different AS has a ROA for a more-specific that conflicts. Complex — investigate further."
- **Correction**: "If no VRP/ROA covers the announced route prefix, the validation state is **NotFound**, not **Invalid**. An **Invalid** result requires at least one covering VRP but no matching VRP."
- **Source**: RFC 6811, Section 2

### 3.3-ebgp-peering-answers.md — Suggests NO_EXPORT as a generic safeguard for IX-learned routes
- **Severity**: minor
- **Location**: Question 1 answer → Critical outbound safeguards
- **Current text**: "NO_EXPORT community on routes learned from IX route servers (prevent re-advertisement to transit)"
- **Correction**: "Prevent peer-to-transit leaks with explicit export policy. Blanket NO_EXPORT on IX-learned routes also prevents advertisement to **customers**, which is usually not what an SP wants. Use route-type-aware export filters instead of universal NO_EXPORT tagging."
- **Source**: RFC 1997; RFC 7454

### 3.4-bgp-policy-and-traffic-engineering.md — Uses AS_PATH prepending in inbound policy for outbound TE
- **Severity**: critical
- **Location**: Outbound Traffic Engineering → AS_PATH Manipulation (for multipath/tiebreaking)
- **Current text**: "route-map TRANSIT-B-IN permit 10 / set as-path prepend 65000 65000 65000"
- **Correction**: "Do not prepend your own AS on inbound policy to influence local outbound path choice. Outbound TE inside your AS should use LOCAL_PREF/weight (and, where relevant, IGP cost). AS_PATH prepending is an **export-side** tool used to influence remote AS decisions for inbound TE."
- **Source**: RFC 4271 decision process and AS_PATH semantics

### 3.4-bgp-policy-and-traffic-engineering.md — Backup selective-announcement example is logically reversed
- **Severity**: critical
- **Location**: Inbound Traffic Engineering → Selective Announcement
- **Current text**: "Transit B (backup): Advertise 203.0.113.0/22 + 203.0.113.0/24 + 203.0.113.4/24 ... When Transit A is up, the aggregate covers everything. If Transit A fails, the more-specifics via Transit B attract traffic (longest match wins, always)."
- **Correction**: "If the more-specifics are advertised via Transit B in steady state, they will attract traffic via Transit B immediately because longest-prefix match wins. If Transit B is truly backup, advertise only the aggregate in steady state and conditionally advertise valid more-specifics on failure, or place the more-specifics on the preferred path instead."
- **Source**: CIDR longest-prefix forwarding behavior; RFC 4632

### 3.4-bgp-policy-and-traffic-engineering.md — Example contains an invalid /24 network
- **Severity**: cosmetic
- **Location**: Inbound Traffic Engineering → Selective Announcement example
- **Current text**: "203.0.113.4/24"
- **Correction**: "Use a valid /24 boundary such as `203.0.113.0/24` or `203.0.114.0/24`."
- **Source**: CIDR prefix boundary rules; RFC 4632

## Clean Files

### 3.1-bgp-fundamentals-at-sp-scale.md — Clean
- No issues found.

### 3.1-bgp-fundamentals-at-sp-scale-answers.md — Clean
- No issues found.

### 3.3-ebgp-peering-theory.md — Clean
- No issues found.

### 3.4-bgp-policy-and-traffic-engineering-theory.md — Clean
- No issues found.

### 3.4-bgp-policy-and-traffic-engineering-answers.md — Clean
- No issues found.
