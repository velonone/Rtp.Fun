# Security policy

## Public security principles

1. **Identity and execution are separate roles.**
2. Plaintext AMS signing material is intended to remain inside the wallet-origin boundary.
3. Signing is narrow: prepared transactions are checked against intent, authorization and policy.
4. Indeterminate execution outcomes are reconciled rather than treated as ordinary failure.
5. Availability is never represented as proof of execution readiness.
6. Public security language must not exceed its evidence.

## Responsible disclosure

Do **not** publish suspected vulnerabilities, exploit steps, credentials or production infrastructure details in a public GitHub issue.

Use the official Responsible Disclosure channel:

https://rtp.fun/docs/disclosure/

The canonical security contact is also published through the website's `/.well-known/security.txt`.

## Scope note

This repository is a public evidence surface. It intentionally omits exploit-enabling implementation detail.
