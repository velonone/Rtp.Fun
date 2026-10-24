# 24 October 2026 product observations

**Issuer:** RTP.FUN. **Type:** first-party, scoped release summary. This is not an independent assessment or a real-time service status report.

## Observed product behavior

- Current public page captures show the homepage, Launchpad and Alliances directory. The original JPEG bytes and capture metadata are described in the [asset record](../../../assets/README.md).
- The known alliance bounty reward now displays **0.001 SOL**, converting the stored base-unit amount instead of appending SOL to the raw integer. Directory and Tasks views were checked. Only one real bounty was available; a second production bounty was not available for sampling.
- Public route previews now use current page imagery and route-specific descriptions. Page HTML and image dimensions were checked using common link-preview user agents. Existing previews cached by external chat services may remain old until those services refresh them.
- Legitimate public link previews return their description again. Old client bundles remain available across deployment so an already-open page can still load its dependent assets.

## Acceptance boundary

A production observation window on 24 October covered public and origin read requests, application health and logs after the repair release. Those checks passed within their stated window. Upstream market quota/stale-data warnings were still observed, so this record does not claim an error-free product or uninterrupted external data.

No new financial transaction, signature, token launch, fundraising activation or airdrop registration was performed for these checks. Previously reviewed on-chain examples apply only to their individual routes; they do not establish that all displayed launch routes have been exercised.

## Public evidence limits

Screenshots establish visible page content at capture time. They do not establish transaction safety, current prices, community earnings, future reward payment or investment value. Internal tests and production observations remain first-party evidence; no independent security report is published with this record.

Raw logs, deployment details, private test fixtures and operational manifests are intentionally excluded under the [publication policy](../../../PUBLICATION_POLICY.md).
