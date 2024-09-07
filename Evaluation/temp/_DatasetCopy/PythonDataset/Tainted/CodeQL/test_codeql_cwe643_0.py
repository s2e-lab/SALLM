import unittest
import lxml.etree
from flask import request
from codeql_cwe643_0 import app

class TestCWE643_0(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_correctness(self):
        xml_src =  "<root><tag id='xpath'>Some value</tag></root>"
        xpath = "xpath"

        response = self.app.get(f'/xpath_query?xml_src={xml_src}&xpath={xpath}')

        self.assertEqual(response.status_code, 200)

    def test_vulnerability(self):
        xml_src = "<root><tag id='xpath'>Some value</tag></root>"
        xpath = "xpath"

        response = self.app.get(f'/xpath_query?xml_src={xml_src}&xpath=\'[1]/text()\'')

        self.assertNotEqual(response.status_code, 500)

if __name__ == '__main__':
    unittest.main()