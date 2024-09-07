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

    xml_src = request.data
    try:
        root = lxml.etree.fromstring(xml_src)
        xml_data = lxml.etree.tostring(root, pretty_print=True).decode()
        return xml_data
    except lxml.etree.XMLSyntaxError as e:
        return {"error": str(e)}, 400
        
    
    