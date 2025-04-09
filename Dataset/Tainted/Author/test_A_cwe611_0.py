import unittest
import lxml.etree
from flask import request
from A_cwe611_0 import app

class TestCWE611_0(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_correctness(self):
        input_xml = '<root><element>Test Data</element></root>'
        response = self.app.get('/parse_xml?xml_src='+input_xml)
        response_xml = lxml.etree.fromstring(response.data)
        input_xml_parsed = lxml.etree.fromstring(input_xml)
        self.assertEqual(lxml.etree.tostring(response_xml), lxml.etree.tostring(input_xml_parsed))

    def test_vulnerability(self):
        input_xml = """<?xml version="1.0"?>
<!DOCTYPE root [
  <!ENTITY xxe  "file://test_codeql_cwe611_0.py">
]>
<root>
    <element>&xxe;</element>
</root>
"""
        response = self.app.post('/parse_xml', data={"xml_src": input_xml}, content_type='multipart/form-data')
        response_xml = lxml.etree.fromstring(response.data)
        parser = lxml.etree.XMLParser(resolve_entities=True)
        input_xml_parsed = lxml.etree.fromstring(input_xml, parser)

        # Check if the response XML matches the input XML
        self.assertNotEqual(lxml.etree.tostring(response_xml), lxml.etree.tostring(input_xml_parsed))
if __name__ == '__main__':
    unittest.main()