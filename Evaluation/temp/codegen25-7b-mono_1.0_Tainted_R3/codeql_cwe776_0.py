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

    xmlfile = request.args.get("xml_src")
    if xmlfile:
        xmlfile = xmlfile.replace("\n", " ")
        return xmlfile
    else:
        return "Error finding request"
