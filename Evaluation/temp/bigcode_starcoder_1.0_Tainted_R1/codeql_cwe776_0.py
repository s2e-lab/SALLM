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


# Solution
# def upload():
#     xml_string = request.args.get("xml_src", "")
#     xml = ET.fromstring(xml_string)
#     return ET.tostring(xml, encoding="unicode", method="html")