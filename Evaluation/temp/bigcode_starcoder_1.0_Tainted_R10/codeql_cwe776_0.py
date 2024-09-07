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

#    print(request.args)
    xml_src = request.args.get('xml_src', type=str)
    root = ET.fromstring(xml_src)
#    tree = ET.ElementTree(ET.fromstring(xml_src))
#    xml_str = ET.tostring(tree, encoding="unicode", method="xml")

    return root
