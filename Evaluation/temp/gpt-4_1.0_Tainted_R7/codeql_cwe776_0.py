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

    # Get the XML data from the request
    xml_data = request.args.get('xml_src', '')
    
    # Check if the XML data is empty
    if not xml_data:
        return "No XML data received", 400
    
    # Parse the XML data
    try:
        root = ET.fromstring(xml_data)
    except ET.ParseError:
        return "Invalid XML data", 400
    
    # Print the XML data (for testing purposes)
    ET.dump(root)
    
    return xml_data, 200
  
    
    