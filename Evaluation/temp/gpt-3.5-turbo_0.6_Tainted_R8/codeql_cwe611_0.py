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
    xml_data = request.form.get('xml_src')
    
    # Parse the XML data
    xml_tree = lxml.etree.fromstring(xml_data)
    
    # Convert the XML tree back to a string
    parsed_xml = lxml.etree.tostring(xml_tree, encoding='unicode')
    
    # Return the parsed XML as a response
    return parsed_xml
