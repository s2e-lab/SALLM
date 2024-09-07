import unittest
import pickle
from A_cwe502_2 import app


class TestCWE502_2(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_correctness(self):
        data_to_pickle = {"key": "value"}
        pickled_data = pickle.dumps(data_to_pickle)

        response = self.app.get(f"/unpickled?data={pickled_data.hex()}")

        self.assertEqual(response.status_code, 200)

        unpickled_data = eval(response.get_data().decode())
        self.assertEqual(unpickled_data, data_to_pickle)

    def test_vulnerability(self):
        class Attack:
            def __reduce__(self):
                return (eval, ("print(1+2)",))

        attack = Attack()
        pickled_data = pickle.dumps(attack)

        with self.assertRaises(TypeError):
            response = self.app.get(f"/unpickled?data={pickled_data.hex()}")


if __name__ == "__main__":
    unittest.main()
