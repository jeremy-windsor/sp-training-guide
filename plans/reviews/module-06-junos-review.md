# Module 06 Junos CLI Syntax Review

## Summary
Reviewed all 18 markdown files under `modules/06-sr/` for Junos-only CLI/config syntax.

Found **4 Junos syntax issues** that are commit-impacting (critical). Most other Junos snippets are syntactically plausible.

---

### [6.1-sr-mpls-fundamentals.md] Line 216 / “How to enable explicit-null” — `explicit-null` placed as a `node-segment` argument
- **Severity**: critical
- **Current text**: "node-segment ipv4-index 4 explicit-null;"
- **Correction**: "`explicit-null;` must be a standalone statement under `protocols isis source-packet-routing`, and `node-segment` must be separate, e.g.:
  `protocols isis { source-packet-routing { explicit-null; node-segment { ipv4-index 4; } } }`"
- **Source**: Juniper TechLibrary — **source-packet-routing (Protocols IS-IS)** (syntax shows `explicit-null;` and `node-segment { ... }` as separate statements):
  https://www.juniper.net/documentation/us/en/software/junos/cli-reference/topics/ref/statement/source-packet-routing-edit-protocols-isis.html

### [6.1-sr-mpls-fundamentals-answers.md] Line 16 / Question 1 remediation — missing protocol hierarchy for SRGB
- **Severity**: critical
- **Current text**: "protocols source-packet-routing srgb start-label 16000 index-range 8000"
- **Correction**: "Include the protocol hierarchy; SRGB is configured under IGP SPRING hierarchy, e.g.:
  `protocols isis source-packet-routing srgb start-label 16000 index-range 8000`
  (or OSPF equivalent)."
- **Source**: Juniper TechLibrary — **source-packet-routing (Protocols IS-IS)** hierarchy is under `[edit protocols isis ...]`:
  https://www.juniper.net/documentation/us/en/software/junos/cli-reference/topics/ref/statement/source-packet-routing-edit-protocols-isis.html

### [6.1-sr-mpls-fundamentals-answers.md] Line 31 / Cause 2 — `node-segment` incorrectly shown under interface hierarchy
- **Severity**: critical
- **Current text**: "protocols isis interface lo0.0 / node-segment ipv4-index <N>"
- **Correction**: "`node-segment` must be configured under `protocols isis source-packet-routing`, not under interface hierarchy, e.g.:
  `protocols isis { source-packet-routing { node-segment { ipv4-index <N>; } } }`"
- **Source**: Juniper TechLibrary — **node-segment (Protocols IS-IS)** hierarchy level includes `[edit protocols isis source-packet-routing]`:
  https://www.juniper.net/documentation/en_US/junos/topics/reference/configuration-statement/node-segment-edit-protocols-isis-source-packet-routing.html

### [6.4-srv6-fundamentals.md] Lines 335–336 / “Enable SRv6 globally” — invalid locator sub-syntax (`prefix` and `end-dt46-sid` placement)
- **Severity**: critical
- **Current text**: "set routing-options source-packet-routing srv6 locator MAIN fc00:0:1::/48" and "set routing-options source-packet-routing srv6 locator MAIN end-dt46-sid"
- **Correction**: "Under current Junos SRv6 CLI, `srv6` uses `block` and `locator` statements (not `locator <name> <prefix>` inline). Use block/locator syntax, e.g.:
  `set routing-options source-packet-routing srv6 block MAIN-BLOCK address fc00:0:1::/48`
  `set routing-options source-packet-routing srv6 locator MAIN`
  (and configure service SIDs in the appropriate service/routing-instance hierarchy)."
- **Source**: Juniper TechLibrary —
  1) **srv6 (Routing Options)** syntax: `srv6 { block ...; locator ...; ... }`
  https://www.juniper.net/documentation/us/en/software/junos/cli-reference/topics/ref/statement/srv6-edit-routing-options-source-packet-routing.html
  2) **locator (Routing Options source-packet-routing srv6)** syntax
  https://www.juniper.net/documentation/us/en/software/junos/cli-reference/topics/ref/statement/locator-edit-routing-options-source-packet-routing-srv6.html
  3) **block (Routing Options source-packet-routing srv6)** syntax
  https://www.juniper.net/documentation/us/en/software/junos/cli-reference/topics/ref/statement/routing-options-source-packet-routing-srv6-block.html
