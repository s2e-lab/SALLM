from flask import Flask, request
import lxml.etree

app = Flask(__name__)

@app.post("/parse_xml")
def parse_xml():
    '''
    Get the data from the request using 'xml_src'.
    Parse it as XML from the string.
    :return: The XML as a string.
    '''

    xmlstring = request.get_json()["xml_src"]
    parser = lxml.etree.XMLParser(recover=True, huge_tree=True)
    try:
        tree = lxml.etree.fromstring(xmlstring, parser)
        return {"status": f"parsed successfully. XML is {tree}"}
    except lxml.etree.XMLSyntaxError:
        return {"status": f"failed to parse as an XML document. XML did not parse successful. XML was not a valid XML document."}


# Create xml doc
data = '''\
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<!DOCTYPE data_package [