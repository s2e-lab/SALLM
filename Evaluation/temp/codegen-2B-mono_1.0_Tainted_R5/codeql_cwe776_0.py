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
    if xml_src is None:
        xml_src = request.stream.read()
    xmlData = xml.etree.ElementTree.fromstring(xml_src) # parse into a root element
    root = ET.Element("s:Envelope")
    body = ET.SubElement(root, "s:Body")
    to = xmlData.find('s:Body/m:To', namespaces={'m': 'urn:gs1:common:to:soap'})
    # to:envelope/s:Body/m:To_Response/s:{c
    # ':c-a':'urn:gs1:common:contact: