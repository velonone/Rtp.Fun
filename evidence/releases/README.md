# Release Evidence

Each public release-evidence directory should contain only sanitized, externally useful artifacts.

Recommended shape:

```text
evidence/releases/<release>/
  manifest.json
  conformance.json
  test-summary.json
  sbom.spdx.json
  SHA256SUMS
```

## Publication rule

Release evidence must be:

- scoped to the exact release;
- generated or reviewed from current evidence;
- scrubbed of credentials and private infrastructure;
- explicit about limitations;
- distinguishable from independent third-party assessment.

Never export raw production logs, credentials, provider quotas, private endpoint inventories or bypass-sensitive verifier traces.
