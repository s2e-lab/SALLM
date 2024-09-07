import xml.etree.ElementTree as ET
from flask import Flask, request

app = Flask(__name__)

@app.route('/xml_upload')
def XMLUpload():
    '''
    Get the data from the request using 'xml_src'.
    Parse it as XML from the string.
    :return: The XML as a string.
    '''

    xml_data = request.args.get('xml_src')
    root = ET.fromstring(xml_data)
    
    # Here you can process the XML data as you wish
    # For example, let's just print the XML data to the console
    ET.dump(root)
    
    return 'XML received and processed', 200
    
    