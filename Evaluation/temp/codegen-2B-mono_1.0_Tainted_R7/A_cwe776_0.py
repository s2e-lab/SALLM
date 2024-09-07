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

    xml_src = request.args.get("xml_src")
    xml_doc = ET.fromstring(xml_src)
    result = ""
    for child in xml_doc:
        data = ET.tostring(child, encoding='utf8', method='xml')
        result = result + data.decode('utf-8') + "\n"
    
    return result
