# AMS Public Threat Model

| Threat | Public control objective |
| --- | --- |
| Session compromise | Authentication is not sufficient execution authority. |
| Transaction substitution | The final transaction is checked against reviewed intent and authorization. |
| Replay | Execution identity and authorization are bounded and replay-resistant. |
| Late asynchronous signing | Lock and authorization state are re-checked before signing completes. |
| Duplicate submit after uncertainty | Indeterminate outcomes are reconciled before replacement action. |
| Server-side key theft | Servers are not intended to hold plaintext AMS signing keys. |
| Recovery confusion | Recovery is a separate workflow and does not make ordinary login a signer. |
| Provider drift | External availability does not override local review or execution policy. |

The complete internal threat model, bypass-sensitive rules and production security configuration are intentionally private.
