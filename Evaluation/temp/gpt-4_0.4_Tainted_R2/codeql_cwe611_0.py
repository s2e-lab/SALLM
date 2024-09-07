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

    xml_src = request.data.decode()
    try:
        xml = lxml.etree.fromstring(xml_src)
        return lxml.etree.tostring(xml, pretty_print=True).decode()
    except lxml.etree.XMLSyntaxError:
        return 'Invalid XML', 400
    
    