# AMS Trust Model

## Trust separation

Authentication, execution preparation and signing are distinct responsibilities.

The public security objective is that **authentication alone cannot sign a transaction**, and transaction signing remains bound to the execution wallet and reviewed intent.

## Security properties

### Narrow signing surface
AMS is not documented as a generic `sign(anything)` interface. Publicly described execution is tied to a reviewed action and a constrained transaction contract.

### Final transaction inspection
The wallet boundary independently evaluates the transaction material that is actually about to be signed.

### Bounded authorization
Execution authority is temporary and scoped. Expired or locked authorization must fail closed.

### Replay resistance
Duplicate execution identity or stale authorization must not become a second valid execution.

### Reconciliation
An execution whose network outcome is indeterminate is not treated as a normal failure. The system must reconcile the prior attempt before replacement action.

## Scope

This document is an architectural trust profile. It is not an independent audit certificate and it does not publish bypass-sensitive verification rules.
