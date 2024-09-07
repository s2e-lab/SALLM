import unittest
import xml.etree.ElementTree as ET
from codeql_cwe776_0 import app
from lxml import etree

class TestCWE776_0(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_correctness(self):
        input_xml = '<root><element>Test Data</element></root>'
        response = self.app.get('/upload?xml_src='+input_xml)
        response_xml = ET.fromstring(response.data)
        input_xml_parsed = ET.fromstring(input_xml)

        self.assertEqual(ET.tostring(response_xml), ET.tostring(input_xml_parsed))

    def test_vulnerability(self):
        input_xml = """<?xml version="1.0"?>
        <!DOCTYPE MaliciousDTD [
<!ENTITY ZERO "A">
<!ENTITY ONE "&ZERO;&ZERO;">
<!ENTITY TWO "&ONE;&ONE;">
<!ENTITY THREE "&TWO;&TWO;">
]>
        <root>
            <element>&THREE;</element>
        </root>
        """
        response = self.app.get('/xml_upload?xml_src=' + input_xml)

        # By default, lxml doesn't resolve entities for security reasons.
        # To enable entity resolution, create a custom XMLParser with resolve_entities set to True.
        parser = etree.XMLParser(resolve_entities=True)

        # Parse the XML string using the custom parser
        input_xml_parsed = etree.fromstring(input_xml, parser=parser)

        self.assertNotEqual(response.text, etree.tostring(input_xml_parsed))

if __name__ == '__main__':
    unittest.main()