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
    
    try:
        # Parse the XML from the string
        root = lxml.etree.fromstring(xml_src)
    
        # Convert the XML to a string
        xml_string = lxml.etree.tostring(root, encoding='utf-8', pretty_print=True)
    
        return xml_string.decode('utf-8')
    except lxml.etree.XMLSyntaxError as e:
        return f"Invalid XML: {str(e)}"
