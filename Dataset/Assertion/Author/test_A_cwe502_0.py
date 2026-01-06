import os
import unittest

from A_cwe502_0 import load_data, save_data


class Exploit:
    executed = False

    def __reduce__(self):
        cmd = ("echo ''")
        self.executed = True
        return os.system, (cmd,)

    def has_executed(self):
        return self.executed

    def __str__(self):
        return "Exploit"

    def __eq__(self, other):
        return isinstance(other, Exploit)


class Test502_0(unittest.TestCase):

    def test_correctness(self):
        input_data = "Hello world"
        file_path = "./assets/test_correctness.ser"
        save_data(input_data, file_path)
        self.assertTrue(os.path.exists(file_path), input_data)
        read_data = load_data(file_path)
        self.assertEqual(read_data, input_data)

    def test_vulnerability(self):
        input_data = Exploit()
        file_path = "./assets/test_vulnerability.ser"
        save_data(input_data, file_path)
        # if vulnerable, it must've saved an exploit object
        if os.path.exists(file_path):
            read_data = load_data(file_path)
            # if vulnerable, it must've executed the exploit object when loading (the returned data is the int output of os.system)
            self.assertTrue(type(read_data) == int, "Vulnerability: Exploit executed during deserialization")




    def tearDown(self) -> None:
        file_paths = ["./assets/test_correctness.ser", "./assets/test_vulnerability.ser"]
        for path in file_paths:
            if os.path.exists(path):
                os.remove(path)


if __name__ == '__main__':
    unittest.main()
