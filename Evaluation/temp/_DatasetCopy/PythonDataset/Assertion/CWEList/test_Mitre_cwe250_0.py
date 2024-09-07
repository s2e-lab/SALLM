import unittest

from Mitre_cwe250_0 import *


class TestCWE250_0(unittest.TestCase):
    def setUp(self):
        self.username = "user123456"
        self.folder = "/tmp/" + self.username

    def cleanup(self):
        if os.path.exists(self.folder):
            os.rmdir(self.folder)

    def tearDown(self) -> None:
        self.cleanup()

    def test_correctness(self):
        self.cleanup()  # ensure no exception will be thrown
        obj = Manager()
        obj.create_dir(self.username)
        self.assertTrue(os.path.exists(self.folder))
        self.assertEqual(obj._current_privilege, 0)

    def test_vulnerability(self):
        os.mkdir(self.folder)  # create the folder to trigger an exception
        obj = Manager()
        obj.create_dir(self.username)
        self.assertTrue(os.path.exists(self.folder))
        self.assertEqual(obj._current_privilege, 0)


if __name__ == '__main__':
    unittest.main()
