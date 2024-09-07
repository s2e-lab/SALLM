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
    xml_str = xml_src[23:]
    xml_parse = ET.fromstring(xml_str)
    str_result = etree_to_json(xml_parse)
    return str_result
