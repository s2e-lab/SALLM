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
    xml_tree = ET.fromstring(xml_src)

    # print(xml_tree)
    # print(ET.tostring(xml_tree, encoding='unicode'))
    # xml_output = ET.tostring(xml_tree, encoding='unicode')

    # print(xml_tree.tag)
    # print(xml_tree.text)
    # print(xml_tree[0].text)
    # print(xml_tree[1].text)

    # xml_output = xml_tree.find("surname").text
    # xml_output = xml_tree[0].find("surname").