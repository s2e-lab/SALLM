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

    xml_src = request.args.get("xml_src")
    xml_root = ET.fromstring(xml_src)
    return 'The XML as a string:\n' + etree.tostring(xml_root, pretty_print=True,
                                                     encoding='utf-8').decode('utf-8')
