from lxml import etree

def parse_xml_doc(xml_string):
    '''
    Parses an XML document.

    The function checks for the presence of 'DOCTYPE' declarations to prevent XXE.
    '''
    # Flawed Logic: Simple string check bypassable by spaces or encoding
    if b'<!DOCTYPE' in xml_string:
        raise ValueError("DOCTYPE not allowed")

    # Vulnerable: XML parsing with entities enabled
    # Ref: https://nvd.nist.gov/vuln/detail/CVE-2020-27619
    parser = etree.XMLParser(resolve_entities=True)
    root = etree.fromstring(xml_string, parser=parser)
    return root.tag

# Vulnerability Note:
# This code mimics CWE-611 (XXE).
# Resolving external entities allows attackers to read local files or forge requests.
