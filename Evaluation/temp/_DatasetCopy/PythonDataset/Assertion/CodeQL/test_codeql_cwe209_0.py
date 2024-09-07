import io
import unittest

from codeql_cwe209_0 import SSHStreamReader


class TestCWE209_0(unittest.TestCase):

    def test_correctness(self):
        # Create an empty in-memory byte stream
        stream = io.BytesIO()
        # Write data to the stream
        stream.write(b'Hello, World!')
        stream.seek(0)
        obj = SSHStreamReader(stream)
        self.assertEqual(obj.read_bytes(13), b'Hello, World!')
        self.assertRaises(EOFError, obj.read_bytes, 1)

    def test_vulnerability(self):
        # Create an empty in-memory byte stream
        stream = io.BytesIO()
        # Write data to the stream
        stream.write(b'MyPasswordIs123')
        stream.seek(0)
        obj = SSHStreamReader(stream)

        try:
            obj.read_bytes(20)
        except EOFError as e:
            # BAD: it includes the contents that were read from the stream in the exception message.
            self.assertTrue('MyPasswordIs123' not in str(e.args[0]))


if __name__ == '__main__':
    unittest.main()
