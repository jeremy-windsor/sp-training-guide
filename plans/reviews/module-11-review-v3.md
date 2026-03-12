# Module 11 Review v3

## Summary
Issues found: **5** remaining technical errors across **3** files.

Reviewed all 11 requested files.

**Verified clean:**
- `11.1-model-driven-networking.md`
- `11.1-model-driven-networking-answers.md`
- `11.1-model-driven-networking-theory.md`
- `11.2-streaming-telemetry-theory.md`
- `11.4-cicd-network-config.md`
- `11.4-cicd-network-config-answers.md`
- `11.5-lab-gnmi-sr-te-automation.md`
- `11.5-lab-gnmi-sr-te-automation-answers.md`

### [11.2-streaming-telemetry.md] — Junos OpenConfig Package Requirement Is Stated Too Absolutely
- **Severity**: minor
- **Current text**: "!! Prerequisite: Junos OpenConfig package must be installed (separate .tgz)"
- **Correction**: "Qualify this by release: on Junos OS 18.3R1 and later, the OpenConfig and Network Agent packages are bundled in the Junos image, so a separate `.tgz` install is not generally required. Only older releases should be described as needing a separate package."
- **Source**: Juniper, *Installing the OpenConfig Package* (states that starting in Junos OS Release 18.3R1, the Junos OS image includes the OpenConfig package)

### [11.2-streaming-telemetry.md] — IOS-XR gRPC Port Note Conflates gNMI/Dial-In With MDT Dial-Out
- **Severity**: minor
- **Current text**: "Unlike IOS-XR (which uses `grpc port 57400` for both gNMI and MDT), Junos uses the extension-service port..."
- **Correction**: "Clarify that IOS-XR `grpc port 57400` is the device-side gRPC server used for dial-in services such as gNMI. IOS-XR MDT dial-out uses the collector port configured under `telemetry model-driven destination-group ... port <port> protocol grpc` and is not inherently tied to local port 57400."
- **Source**: Cisco IOS XR *Programmability Configuration Guide* (gRPC server default listening port 57400); Cisco IOS XR *Telemetry Configuration Guide* (MDT dial-out destination-group uses configured collector IP/port)

### [11.3-sr-te-controller-integration.md] — Junos BGP-LS Enablement Uses the Wrong Hierarchy/Mechanism
- **Severity**: critical
- **Current text**: "export EXPORT-BGP-LS;"
- **Correction**: "Do not present IS-IS `export` as the BGP-LS enablement mechanism. On Junos, BGP-LS reads topology from `lsdist.0`; the documented workflow is to import IGP topology under `[edit protocols mpls traffic-engineering database import igp-topology] set bgp-ls`, then advertise the traffic-engineering family to the BGP-LS peer."
- **Source**: Juniper, *Link-State Distribution Using BGP*; Juniper, *MPLS Traffic Engineering Configuration* (documents `set bgp-ls` under `[edit protocols mpls traffic-engineering database import igp-topology]`)

### [11.3-sr-te-controller-integration.md] — Junos ODN Example Uses an Unsupported/Undocumented Knob and Wrong SR-TE Hierarchy
- **Severity**: critical
- **Current text**: "routing-options { segment-routing { traffic-engineering { egress-policy { color 100; } } } }"
- **Correction**: "Replace this with Junos-documented color-based traffic-engineering guidance. Junos color steering is documented around resolution maps / transport-class resolution and SR-TE under the `protocols source-packet-routing` hierarchy; `routing-options segment-routing traffic-engineering egress-policy color ...` is not the documented Junos ODN configuration."
- **Source**: Juniper, *Color-Based Traffic Engineering Configuration*; Juniper CLI reference for `source-packet-routing (Segment Routing Traffic Engineering)`

### [11.3-sr-te-controller-integration-answers.md] — IOS-XR SR-TE Metric Keyword Uses the Wrong CLI Value
- **Severity**: minor
- **Current text**: "metric type delay    ! min-delay constraint"
- **Correction**: "Use `metric type latency` for IOS-XR SR-TE ODN/policy examples unless you are explicitly documenting a release-specific alternate syntax. This also matches the main lesson file."
- **Source**: Cisco IOS XR *Segment Routing Configuration Guide* / command reference (documents `metric type { igp | te | latency }` for SR-TE policy path computation)
