# Public architecture

This is a **trust-boundary view**, not a production topology map.

```mermaid
flowchart LR
    A[Market + community inputs] --> B[Discovery + coordination]
    B --> C[Reviewed user intent]
    C --> D[Execution preparation]
    D --> E[AMS wallet-origin boundary]
    E --> F[Local signing]
    F --> G[Signed relay]
    G --> H[Network / integrated venue]
    H --> I[Receipt + reconciliation]
```

## Public boundaries

### Product surface
Owns the visible user workflow, authenticated session context and reviewed intent.

### AMS execution boundary
Owns sensitive wallet duties, authorization state, transaction inspection and local signing.

### Server execution boundary
May prepare, validate, authorize and relay execution material. The public model does not require the server to possess an AMS private key.

### External systems
Market-data, risk, network and venue dependencies are treated as external systems. Their private identities, commercial configuration and failover order are not part of this public architecture.

## Deliberately omitted

- private data-source identities and failover order;
- provider quotas and commercial routing priority;
- production hostnames, topology and credentials;
- full private API inventories;
- anti-abuse thresholds;
- database structure;
- bypass-sensitive verifier fingerprints;
- unpublished automation and risk parameters.

The public repository exists to make trust claims reviewable without publishing the machinery needed to attack or reproduce the private operating stack.
