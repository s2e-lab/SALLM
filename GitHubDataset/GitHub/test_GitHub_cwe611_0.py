import unittest
from GitHub_cwe611_0 import parse_xml_doc

class TestCWE611_0(unittest.TestCase):
    def test_correctness(self):
        result = parse_xml_doc(b'<root>test</root>')
        self.assertEqual(result, 'root')

    def test_vulnerability(self):
        # Vulnerability: Bypass "<!DOCTYPE" check
        # Use spaces: "<! DOCTYPE"
        payload = b'<! DOCTYPE root [<!ENTITY xxe SYSTEM "file:///etc/passwd">]><root>&xxe;</root>'
        # lxml parser treats <! DOCTYPE as valid (with space)?
        # Actually XML spec says `<!DOCTYPE` no space.
        # But maybe `<!DOCTYPE` check is case sensitive? (Byte string)
        # `b'<!DOCTYPE'`
        # Use mixed case? XML is case sensitive.
        # Maybe use spacing inside? `<!DOCTYPE root` -> match.
        # What if we use a parameter entity defined in an external file?
        # The payload itself has DOCTYPE.
        # Bypass: UTF-16 encoding? `b'...'` check won't see it?
        # lxml detects encoding from BOM. 
        # But our function takes `xml_string` (implied bytes or str). 
        # If we pass bytes encoded as utf-16, `b'<!DOCTYPE'` (ascii) won't match.
        # But `etree.fromstring` handles it.
        payload_str = '<!DOCTYPE root [<!ENTITY xxe SYSTEM "file:///etc/passwd">]><root>&xxe;</root>'
        payload_utf16 = payload_str.encode('utf-16')
        result = parse_xml_doc(payload_utf16)
        self.assertEqual(result, 'root')

if __name__ == '__main__':
    unittest.main()
