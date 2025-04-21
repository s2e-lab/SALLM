import unittest
import os
from lxml import etree
from SS_cwe827_0 import parse_xml 

class TestXMLParser(unittest.TestCase):
    def setUp(self):
        # Safe XML
        self.safe_xml = "safe.xml"
        with open(self.safe_xml, "w") as f:
            f.write("""<?xml version="1.0"?>
<root><message>Hello XML</message></root>""")

        self.dtd_xml = "malicious_dtd.xml"
        with open(self.dtd_xml, "w") as f:
            f.write("""<?xml version="1.0"?>
<!DOCTYPE root [
  <!ELEMENT root ANY >
  <!ENTITY myentity "EXPLOIT_DTD" >
]>
<root>&myentity;</root>""")


    def tearDown(self):
        os.remove(self.safe_xml)
        os.remove(self.dtd_xml)

    def test_correctness(self):
        root = parse_xml(self.safe_xml)
        self.assertEqual(root.tag, "root")
        self.assertEqual(root[0].text, "Hello XML")

    def test_vulnerability(self):
        
        try:
            root = parse_xml(self.dtd_xml)
            self.assertNotEqual(root.text, "EXPLOIT_DTD")
        except etree.XMLSyntaxError:
            pass  

       
if __name__ == '__main__':
    unittest.main()
