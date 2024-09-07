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
    tree = ET.ElementTree(ET.fromstring(xml_src))
    root = tree.getroot()
    
    # Convert the XML data back to a string and return
    return ET.tostring(root, encoding='utf8', method='xml').decode()
