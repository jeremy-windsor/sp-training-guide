# Module 11 (Automation) — Technical Accuracy Review

## Summary
- **Files reviewed**: 11
- **Issues found**: 11
- **Severity counts**: critical **2**, minor **9**
- **Files needing fixes**:
  - 11.1-model-driven-networking.md
  - 11.1-model-driven-networking-theory.md
  - 11.1-model-driven-networking-answers.md
  - 11.2-streaming-telemetry-theory.md
  - 11.5-lab-gnmi-sr-te-automation.md
- **No technical issues found in this pass**:
  - 11.2-streaming-telemetry.md
  - 11.3-sr-te-controller-integration.md
  - 11.3-sr-te-controller-integration-answers.md
  - 11.4-cicd-network-config.md
  - 11.4-cicd-network-config-answers.md
  - 11.5-lab-gnmi-sr-te-automation-answers.md

### [11.1-model-driven-networking-theory.md] — NETCONF is described as having a standalone `rollback` operation
- **Severity**: minor
- **Current text**: "NETCONF (RFC 6241, 2011) is the configuration management protocol. It runs over SSH, uses XML-encoded RPCs, and provides transactional configuration operations (get, edit-config, commit, rollback) against YANG-modeled datastores."
- **Correction**: "NETCONF does not define a standalone `<rollback>` RPC. Replace `rollback` with standards-based operations/capabilities such as `discard-changes`, `validate`, and `rollback-on-error` semantics, or describe rollback as a vendor workflow rather than a base NETCONF operation."
- **Source**: RFC 6241 Section 7; RFC 6241 Section 8.5

### [11.1-model-driven-networking-theory.md] — NETCONF filtering is overstated as XPath by default
- **Severity**: minor
- **Current text**: "NETCONF uses XPath (XML Path Language) for filtering data in `get` and `get-config` operations."
- **Correction**: "NETCONF supports subtree filtering by default. XPath filtering is optional and requires the `:xpath` capability. A correct replacement is: `NETCONF supports subtree filtering by default and XPath filtering when the server advertises :xpath.`"
- **Source**: RFC 6241 Section 6

### [11.1-model-driven-networking.md] — Wrong RFC cited for `ietf-bgp`
- **Severity**: minor
- **Current text**: "1. **IETF standard models** — `ietf-interfaces` (RFC 8343), `ietf-routing` (RFC 8349), `ietf-bgp` (RFC 9657). Lowest common denominator, multi-vendor."
- **Correction**: "Remove the RFC 9657 citation. RFC 9657 is not a BGP YANG model RFC. If you want to reference the IETF BGP YANG work, cite the active Internet-Draft (`draft-ietf-idr-bgp-model`) or omit an RFC number here. The reference list entry `RFC 9657 — YANG Model for BGP` also needs the same fix."
- **Source**: RFC 9657; IETF `draft-ietf-idr-bgp-model`

### [11.1-model-driven-networking.md] — Junos `system services rest` is mislabeled as RESTCONF
- **Severity**: minor
- **Current text**: "# RESTCONF (Junos 21.2+)\nset system services rest http port 8080\nset system services rest https port 8443\nset system services rest https server-certificate rest-cert"
- **Correction**: "Relabel this as Junos REST API, or replace it with a verified RFC 8040 RESTCONF example for a specific Junos platform/release. Juniper documents `[edit system services rest]` as the Junos REST API used to submit RPC commands over HTTP/HTTPS, not generic RFC 8040 RESTCONF."
- **Source**: RFC 8040; Juniper *Understanding the REST API*; Juniper *Configuring the REST API*

### [11.1-model-driven-networking.md] — ncclient `edit_config` example claims the client auto-wraps `<config>`
- **Severity**: critical
- **Current text**: "# NOTE: ncclient adds <config> wrapper — do NOT include it in the XML"
- **Correction**: "Do not state that ncclient auto-wraps the payload. For `edit_config`, the payload must be rooted in `<config>...</config>`. As written, the sample is misleading and likely to fail if copied verbatim."
- **Source**: RFC 6241 Section 7.2; ncclient `EditConfig` documentation (`config` must be rooted in the `config` element)

### [11.1-model-driven-networking-answers.md] — NETCONF `operation` attribute is shown without the NETCONF namespace
- **Severity**: critical
- **Current text**: "<neighbors operation=\"replace\">"
- **Correction**: "Qualify the attribute in the NETCONF namespace, for example `<neighbors nc:operation=\"replace\">` with `xmlns:nc=\"urn:ietf:params:xml:ns:netconf:base:1.0\"`. Unprefixed attributes are not placed in the default XML namespace."
- **Source**: RFC 6241 Section 7.2; W3C Namespaces in XML 1.0

### [11.1-model-driven-networking-answers.md] — Junos RESTCONF support claim is misleading
- **Severity**: minor
- **Current text**: "| RESTCONF | Supported but less common in SP deployments | Supported (Junos 18.3+) |"
- **Correction**: "Do not present Junos `rest` service as RFC 8040 RESTCONF without a platform/release-specific citation. Reword this as `Junos REST API available` or provide a verified RESTCONF support statement tied to exact Junos releases and implementation details."
- **Source**: RFC 8040; Juniper *Understanding the REST API*

### [11.2-streaming-telemetry-theory.md] — RFC 5277 is treated as the main IETF datastore-streaming standard
- **Severity**: minor
- **Current text**: "Two primary protocols implement streaming telemetry: **gNMI Subscribe** (OpenConfig, gRPC-based) and **NETCONF Notifications** (IETF, RFC 5277)."
- **Correction**: "For IETF-standard datastore streaming, reference Subscribed Notifications / YANG-Push (RFC 8639 and RFC 8641). RFC 5277 defines event notifications and replay, but periodic/on-change datastore subscriptions are standardized later in RFC 8639/8641."
- **Source**: RFC 5277; RFC 8639; RFC 8641

### [11.2-streaming-telemetry-theory.md] — gNMI default encoding is incorrectly stated as protobuf
- **Severity**: minor
- **Current text**: "- Default encoding for gNMI."
- **Correction**: "Do not state protobuf as the default encoding for gNMI. gNMI supports multiple encodings, and when `GetRequest.encoding` is omitted, the specification says JSON MUST be used. If you want to say protobuf is commonly used for high-volume streaming, say that instead."
- **Source**: OpenConfig gNMI Specification v0.10.0 Section 3.3.1; `gnmi.proto` `enum Encoding`

### [11.5-lab-gnmi-sr-te-automation.md] — Lab objective mislabels gNMI as dial-out
- **Severity**: minor
- **Current text**: "1. gNMI dial-out streaming from two IOS-XR routers (P1, P2)"
- **Correction**: "Change this to a dial-in description, e.g. `gNMI dial-in subscriptions from the automation host/gnmic to two IOS-XR routers (PE1, PE2)`. In gNMI, the `Subscribe` RPC is client-initiated; vendor dial-out telemetry is a separate mechanism."
- **Source**: OpenConfig gNMI Specification v0.10.0 Section 3.5

### [11.5-lab-gnmi-sr-te-automation.md] — Junos is incorrectly described as using `netconf-yang`
- **Severity**: minor
- **Current text**: "Port the NETCONF config push to work against Junos devices. Junos uses `netconf-yang` via Junos-native YANG (`junos-conf-root`) or PyEZ."
- **Correction**: "Replace this with Junos-accurate wording. `netconf-yang` is Cisco CLI terminology, not Junos. Junos NETCONF is enabled under `[edit system services netconf ssh]`; Junos-native XML/YANG payload handling should be described separately from Cisco `netconf-yang` syntax."
- **Source**: Juniper *Establish an SSH Connection for a NETCONF Session*; Juniper `ssh (NETCONF)` CLI reference
