# 25 October 2026 public-repository corrections

## Public scanner

The public-text scanner now covers additional explicit private-key block
headers and nonempty triple-quoted key assignments, including multiline values.
Existing placeholder rules, ordinary assignment handling and unreadable-file
guards remain in place. Diagnostics identify the file and category without
printing a matched value.

The regression suite uses clearly synthetic, unusable fixture content only.
It is included in the existing verification workflow and requires only Python's
standard library and Git. No application dependency or production behavior
changes are included in this correction.

## Account access wording

Product copy now distinguishes the public overview, user guide and supported
shared links from directories that require an RTP.FUN account. Screenshot
captions do not imply signed-out access. No application access rule was changed.
Existing public links returned successful document responses; those responses
alone do not prove guest access or completed product workflows.

## Verification boundary

The two reported regressions were reproduced in an isolated verification
environment before the repair. The focused pre-repair command ran two test
methods and recorded five failing assertions across the PGP and quoted-value
cases. Post-repair verification in the isolated environment passed all eight
regression test methods, with zero failures or skips. The public-text scanner,
JSON/SVG and Python syntax checks, and assurance-language check also exited 0.
These results cover this public repository, not the private application's
transaction safety or an independent security assessment.

GitHub workflow verification is not represented as green. The isolated checks
above are reported separately from GitHub CI. No real signing material,
financial action, local test/build or production configuration change was used
for this work.
