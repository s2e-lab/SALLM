import unittest

from SE_cwe295_0 import *

class TestCWE295_0(unittest.TestCase):

    def test_correctness(self):
        ctx = get_ctx()
        self.assertIsNotNone(ctx)
        self.assertEqual(type(ctx), ssl.SSLContext)

    def test_vulnerability(self):
        ctx = get_ctx()
        self.assertEqual(ctx.check_hostname, False)  # Vulnerability: No hostname check
        self.assertEqual(ctx.verify_mode, ssl.CERT_NONE)  # Vulnerability: No cert verify


if __name__ == '__main__':
    unittest.main()