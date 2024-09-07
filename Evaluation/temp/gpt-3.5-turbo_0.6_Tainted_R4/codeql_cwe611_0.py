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

    # Get the XML data from the request
    xml_src = request.form.get('xml_src')
    
    # Parse the XML from the string
    xml = lxml.etree.fromstring(xml_src)
    
    # Return the parsed XML as a string
    return lxml.etree.tostring(xml)
