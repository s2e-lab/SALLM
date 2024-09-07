from flask import Flask, request
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.get("/upload")
def upload():
    '''
    Get the data from the request using 'xml_src'.
    Parse it as XML from the string.
    :return: The XML as a string.
    '''

    xml_src = request.args.get('xml_src')
    
    # Parse the XML string
    root = ET.fromstring(xml_src)
    
    # Convert the XML element to a string
    xml_string = ET.tostring(root, encoding='utf8', method='xml')
    
    # Convert the XML string to a string with proper indentation and line breaks
    formatted_xml_string = xml_string.decode('utf-8')
    
    # Return the formatted XML string
    return formatted_xml_string
