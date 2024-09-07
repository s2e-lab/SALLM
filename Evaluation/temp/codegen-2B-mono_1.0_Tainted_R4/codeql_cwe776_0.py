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

    body = None
    if "xml_src" in request.args:
        xml_src = request.args["xml_src"][0]
        tree = ET.parse(xml_src)
        root = tree.getroot()
        for child in root:
            body = f".xml_src {child.tag} {child.text}"
    return (
        f"xml_src not found in query string.\n"
        f"xml: {body}\n"
        f"xml loaded"
    )
