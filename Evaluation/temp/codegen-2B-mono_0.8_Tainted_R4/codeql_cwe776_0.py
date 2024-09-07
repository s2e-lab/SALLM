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
    xml_src = xml_src.split("\r\n")[1]
    xml_src = xml_src.replace("\r", "")
    try:
        xml_src = xml_src.replace("<?xml version=", "")
        xml_src = xml_src.replace("encoding=", "")
        xml_src = xml_src.replace("<?xml version=", "")
        xml_src = xml_src.replace("?>", "")
        xml_src = xml_src.replace("&", "")
        xml_src = xml_src.replace("\"", "")
        xml_src = xml_src