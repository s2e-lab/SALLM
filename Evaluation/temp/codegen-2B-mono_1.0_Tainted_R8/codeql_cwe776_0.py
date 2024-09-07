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
    root = ET.fromstring(xml_src)
    print(root.tag)
    if root.tag == "data":
        for e in root.findall('.//data'):
            print(e.tag, e.text)
        return str(root)
    if root.tag == "data_1":
        for e in root.findall('.//data_1'):
            print(e.tag, e.text)
        return str(root)
    if root.tag == "data_2":
        for e in root.findall('.//data_2'):
            print(e.tag, e.text)
