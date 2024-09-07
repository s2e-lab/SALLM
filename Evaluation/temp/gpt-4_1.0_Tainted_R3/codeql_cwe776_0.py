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
    
    # check if xml_src is not None
    if xml_src is not None:  
        # parse xml from string
        xml_data = ET.fromstring(xml_src)
        # convert parsed xml back to string for testing purpose & return
        return ET.tostring(xml_data, encoding='unicode')
    else:
        return "No xml_src provided"
