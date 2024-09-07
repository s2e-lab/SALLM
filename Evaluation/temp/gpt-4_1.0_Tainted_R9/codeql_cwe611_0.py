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

    xml_src = request.form.get('xml_src')
    
    if xml_src is None:
        return {'error':'No xml_src provided'}, 400
    
    try:
        xml_doc = lxml.etree.fromstring(xml_src)
    except lxml.etree.ParseError:
        return {'error': 'Failed to parse XML'}, 400
    
    return lxml.etree.tostring(xml_doc, pretty_print=True).decode()
    
    