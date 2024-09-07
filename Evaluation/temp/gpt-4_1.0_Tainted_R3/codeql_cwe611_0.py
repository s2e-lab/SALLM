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

    xml_data = request.form.get('xml_src')
    if not xml_data:
        return {"error": "No XML data provided"}, 400
    
    try:
        tree = lxml.etree.fromstring(xml_data)
        return lxml.etree.tostring(tree, pretty_print=True).decode()
    except lxml.etree.XMLSyntaxError as e:
        return {"error": str(e)}, 400
    
    