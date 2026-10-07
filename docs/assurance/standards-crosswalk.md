# Standards Crosswalk

This crosswalk identifies standards and specifications that are technically relevant to the public trust profile. It does **not** imply certification by the standards bodies.

| Control area | Reference | Public wording |
| --- | --- | --- |
| Password-based KDF | RFC 9106 / Argon2id | Designed Against |
| Authenticated encryption | AES-GCM / NIST SP 800-38D | Designed Against |
| Web application verification | OWASP ASVS 5.0.0 | Mapped controls |
| Secure software development | NIST SSDF SP 800-218 v1.1 | Process crosswalk |
| Build provenance | SLSA v1.2 | Release-evidence target |
| SBOM | SPDX 3.0 / ISO/IEC 5962:2021 | Evidence-format target |
| Wallet derivation | BIP-39 / BIP-32 / SLIP-0010 | Protocol profile |

## Language rule

Use **Mapped to**, **Designed Against**, **Conformance Evidence**, **Production Observed** or **Independently Assessed**.

Do not use **certified**, **ISO certified**, **NIST certified**, **OWASP certified**, **SLSA certified** or **fully audited** unless a separately verifiable certification or assessment exists for the named scope.
