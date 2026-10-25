"""Exercise the public scanner with synthetic, unusable fixture content only."""

import pathlib
import subprocess
import sys
import tempfile
import unittest


SCANNER = pathlib.Path(__file__).with_name("check_public_secrets.py")
SYNTHETIC_VALUE = "SYNTHETIC_UNUSABLE_SCANNER_FIXTURE_NOT_A_CREDENTIAL"


def assignment(value):
    # Assemble sensitive-looking syntax at runtime so the fixture source itself
    # remains publishable by the same scanner it exercises.
    return "API" + "_KEY = " + value


def armored_header(label):
    return "-----" + "BEGIN " + label + "-----\n" + SYNTHETIC_VALUE + "\n"


class PublicSecretScannerTest(unittest.TestCase):
    def scan(self, content, name="fixture.txt"):
        with tempfile.TemporaryDirectory(prefix="rtp-public-scanner-") as temporary:
            root = pathlib.Path(temporary)
            subprocess.run(
                ["git", "init", "--quiet", str(root)], check=True, capture_output=True
            )
            payload = content.encode("utf-8") if isinstance(content, str) else content
            (root / name).write_bytes(payload)
            result = subprocess.run(
                [sys.executable, str(SCANNER), "--root", str(root)],
                capture_output=True,
                text=True,
                timeout=15,
            )
        self.assertFalse(SYNTHETIC_VALUE in result.stdout, "scanner disclosed a synthetic fixture in stdout")
        self.assertFalse(SYNTHETIC_VALUE in result.stderr, "scanner disclosed a synthetic fixture in stderr")
        return result

    def assert_rejected(self, content, category, name="fixture.txt"):
        result = self.scan(content, name)
        self.assertEqual(result.returncode, 1)
        self.assertIn('"category": "' + category + '"', result.stdout)

    def test_pgp_private_header_is_rejected(self):
        self.assert_rejected(armored_header("PGP PRIVATE KEY BLOCK"), "private-key")

    def test_nonempty_triple_quoted_assignment_is_rejected(self):
        for quote in ['"' * 3, "'" * 3]:
            for value in [SYNTHETIC_VALUE, "\n" + SYNTHETIC_VALUE + "\n"]:
                with self.subTest(quote=quote, multiline=value.startswith("\n")):
                    self.assert_rejected(assignment(quote + value + quote), "api-key-assignment")

    def test_unclosed_nonempty_triple_quoted_assignment_is_rejected(self):
        for quote in ['"' * 3, "'" * 3]:
            with self.subTest(quote=quote):
                self.assert_rejected(assignment(quote + SYNTHETIC_VALUE), "api-key-assignment")

    def test_existing_private_header_formats_stay_rejected(self):
        for label in ["PRIVATE KEY", "RSA PRIVATE KEY", "OPENSSH PRIVATE KEY", "EC PRIVATE KEY", "DSA PRIVATE KEY", "ENCRYPTED PRIVATE KEY"]:
            with self.subTest(label=label):
                self.assert_rejected(armored_header(label), "private-key")

    def test_ordinary_nonempty_assignments_stay_rejected(self):
        for value in [SYNTHETIC_VALUE, '"' + SYNTHETIC_VALUE + '"', "'" + SYNTHETIC_VALUE + "'", '\n"' + SYNTHETIC_VALUE + '"']:
            with self.subTest(form=value[0]):
                self.assert_rejected(assignment(value), "api-key-assignment")

    def test_empty_values_and_explicit_placeholders_are_allowed(self):
        for value in ['""', "''", '""""""', "'" * 6, '"${SCANNER_FIXTURE}"', '"<REDACTED>"', '"""${SCANNER_FIXTURE}"""']:
            with self.subTest(form=value):
                self.assertEqual(self.scan(assignment(value)).returncode, 0)

    def test_plain_text_and_public_key_headers_are_allowed(self):
        self.assertEqual(self.scan("RTP.FUN public product documentation.\n").returncode, 0)
        self.assertEqual(self.scan(armored_header("PGP PUBLIC KEY BLOCK")).returncode, 0)

    def test_existing_unreadable_text_and_disguised_image_guards_remain_closed(self):
        self.assert_rejected(b"\xff\xfe\x00", "non-utf8-text")
        self.assert_rejected(b"not an image", "invalid-binary-image", "fixture.png")


if __name__ == "__main__":
    unittest.main()
