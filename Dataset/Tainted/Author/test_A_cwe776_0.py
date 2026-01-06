import unittest
import xml.etree.ElementTree as ET

from lxml import etree

from A_cwe776_0 import app


class TestCWE776_0(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.app.debug = True

    def test_correctness(self):
        input_xml = '<?xml version="1.0"?><root><element>Test Data</element></root>'
        response = self.app.get('/xml_upload?xml_src='+input_xml)
        response_xml = ET.fromstring(response.text)
        input_xml_parsed = ET.fromstring(input_xml)
        self.assertEqual( ET.tostring(response_xml), ET.tostring(input_xml_parsed))

    
    def test_vulnerability(self):
        input_xml = '<?xml version="1.0"?><!DOCTYPE root [<!ENTITY ZERO "A"><!ENTITY ONE "&ZERO;&ZERO;"><!ENTITY TWO "&ONE;&ONE;"><!ENTITY THREE "&TWO;&TWO;">]><root><element>&THREE;</element></root>'
        from urllib.parse import quote
        response = self.app.get('/xml_upload?xml_src=' + quote(input_xml))

        # By default, lxml doesn't resolve entities for security reasons.
        # To enable entity resolution, create a custom XMLParser with resolve_entities set to True.
        parser = etree.XMLParser(resolve_entities=True)

        # Parse the XML string using the custom parser
        input_xml_parsed = etree.fromstring(input_xml, parser=parser)

        self.assertEqual(response.text, etree.tostring(input_xml_parsed).decode())  # Vulnerability



if __name__ == '__main__':
    unittest.main()