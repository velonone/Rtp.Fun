"""Reject obvious secret material without echoing matching content to CI logs."""

import argparse
import json
import pathlib
import re
import subprocess
import sys


PRIVATE_KEY = re.compile(
    r"-----BEGIN (?:[A-Z0-9]+ )*PRIVATE KEY(?: BLOCK)?-----"
)
API_KEY_ASSIGNMENT = re.compile(
    r"\bapi[_-]?key[\"']?\s*[:=]\s*"
    r'(?:"""(?P<triple_double>[\s\S]*?)(?:"""|\Z)'
    r"|'''(?P<triple_single>[\s\S]*?)(?:'''|\Z)"
    r'|"(?P<double>(?:\\.|[^"\\])*)"'
    r"|'(?P<single>(?:\\.|[^'\\])*)'"
    r"|(?P<bare>[^\s,;\]]+))",
    re.IGNORECASE,
)
PLACEHOLDER = re.compile(
    r"(?:\$\{[A-Za-z_][A-Za-z0-9_]*\}"
    r"|<(?:PLACEHOLDER|API_KEY|YOUR_API_KEY|REDACTED)>)"
)
BINARY_IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".ico", ".avif"}


def is_known_binary_image(suffix, data):
    if suffix == ".png":
        return data.startswith(b"\x89PNG\r\n\x1a\n")
    if suffix in {".jpg", ".jpeg"}:
        return data.startswith(b"\xff\xd8\xff")
    if suffix == ".webp":
        return data.startswith(b"RIFF") and data[8:12] == b"WEBP"
    if suffix == ".gif":
        return data.startswith((b"GIF87a", b"GIF89a"))
    if suffix == ".ico":
        return data.startswith(b"\x00\x00\x01\x00")
    if suffix == ".avif":
        return data[4:8] == b"ftyp" and data[8:12] in {b"avif", b"avis"}
    return False


def report(name, category, line=None):
    metadata = {"file": name, "category": category}
    if line is not None:
        metadata["line"] = line
    print(json.dumps(metadata))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=pathlib.Path, default=pathlib.Path.cwd())
    args = parser.parse_args()
    root = args.root.resolve()
    tracked = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
        cwd=root,
        check=True,
        capture_output=True,
    ).stdout
    findings = 0
    for name in sorted(set(tracked.decode("utf-8").split("\0")) - {""}):
        path = root / name
        if path.is_symlink():
            report(name, "symlink-not-scanned")
            findings += 1
            continue
        try:
            data = path.read_bytes()
        except OSError:
            report(name, "unreadable-file")
            findings += 1
            continue
        if path.suffix.lower() in BINARY_IMAGE_SUFFIXES:
            if not is_known_binary_image(path.suffix.lower(), data):
                report(name, "invalid-binary-image")
                findings += 1
            continue
        try:
            content = data.decode("utf-8")
        except UnicodeDecodeError:
            report(name, "non-utf8-text")
            findings += 1
            continue
        for match in PRIVATE_KEY.finditer(content):
            report(name, "private-key", content.count("\n", 0, match.start()) + 1)
            findings += 1
        for match in API_KEY_ASSIGNMENT.finditer(content):
            value = next(value for value in match.groups() if value is not None)
            if value and not PLACEHOLDER.fullmatch(value):
                report(name, "api-key-assignment", content.count("\n", 0, match.start()) + 1)
                findings += 1
    if findings:
        print("Potential secret material found; matching values are not printed.")
        return 1
    print("Public text scan passed; binary assets require separate visual review.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
