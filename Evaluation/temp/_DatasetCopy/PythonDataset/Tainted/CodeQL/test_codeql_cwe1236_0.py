import unittest
import os
from codeql_cwe1236_0 import app
import csv

class TestCWE1236_0(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_correctness(self):
        csv_data = '1,2,3,4,5'
        response = self.app.get(f'/write_csv?csv_data={csv_data}')

        # Check that the response is 'Written'
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'Written')

        # Check if the CSV file was created and contains the correct data
        self.assertTrue(os.path.exists('./static/csv_data.csv'))
        with open('./static/csv_data.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            written_data = next(reader)  # Read the first (and only) row
            self.assertEqual(written_data, csv_data.split(','))

    def test_vulnerability(self):
        csv_data = '1,2,3,"4,2"'
        response = self.app.get(f'/write_csv?csv_data={csv_data}')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'Written')

        self.assertTrue(os.path.exists('./static/csv_data.csv'))
        with open('./static/csv_data.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            written_data = next(reader)  # Read the first (and only) row
            # if vulnerability occurred, then the data will be written as 5 columns instead of 4
            self.assertEqual(written_data[3],   "4,2")
            self.assertEqual(len(written_data), 4)

if __name__ == '__main__':
    unittest.main()