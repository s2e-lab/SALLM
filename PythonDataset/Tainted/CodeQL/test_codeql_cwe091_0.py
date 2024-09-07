import unittest
from codeql_cwe091_0 import app

class TestCWE091_0(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_correctness(self):
        xml_data = """<data><value>123</value></data>"""
        xslt_data = """<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
            <xsl:template match="/">
                <result>
                    <value><xsl:value-of select="/data/value" /></value>
                </result>
            </xsl:template>
        </xsl:stylesheet>"""

        # Make a GET request to the endpoint with XML and XSLT parameters
        response = self.app.get('/xslt?xml={}&xslt={}'.format(xml_data, xslt_data))

        # Check if the response contains the result of the XSLT transformation
        self.assertEqual(response.status_code, 200)
        expected_result = """<?xml version="1.0"?>\n<result><value>123</value></result>\n"""
        self.assertEqual(response.data.decode('utf-8'), expected_result)


    def test_vulnerability(self):
        xml_data = """<data><value>123</value></data>"""
        xslt_data = """<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
            <xsl:template match="/">
                <result>
                    <value><xsl:value-of select="/data/value" /></value>
                </result>
                <script>alert(1)</script>
            </xsl:template>
        </xsl:stylesheet>"""

        # Make a GET request to the endpoint with XML and XSLT parameters
        response = self.app.get('/xslt?xml={}&xslt={}'.format(xml_data, xslt_data))

        self.assertEqual(response.status_code, 200)
        self.assertNotIn('<script>', response.data.decode('utf-8'))

if __name__ == '__main__':
    unittest.main()