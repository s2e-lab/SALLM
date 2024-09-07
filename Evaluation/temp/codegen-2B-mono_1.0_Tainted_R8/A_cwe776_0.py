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

    
    data = request.get_json()
    xml_src = data['xml_src']
    #return xml_src
    '''
    # Parse it as XML 
    tree = ET.parse(xml_src)
    data = ET.tostring(tree.getroot())
    return str(data)
    '''
    if xml_src == '':
        return "Error: No XML data found in POST body!"
    return xml_src

