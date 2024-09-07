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

    data = request.args["xml_src"]
    root = ET.fromstring(data.strip())
    return str(ET<mask_1><sep><mask_1>.tostring(root, encoding="UTF-8", method='html'), 'utf-8')
