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

#    xml_data = request.args.get('xml_src')
#    xml_root = ET.fromstring(xml_data)
#    return ET.tostring(xml_root, encoding='unicode', method='xml')
    return "<xml>Hello World!</xml>"

