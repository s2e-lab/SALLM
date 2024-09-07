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
    xml_src = xml_src.replace("&lt;", "<")
    xml_src = xml_src.replace("&gt;", ">")
    xml_src = xml_src.replace("&quot;", "\"")
    xml_src = xml_src.replace("&apos;", "'")
    xml_src = xml_src.replace("&amp;", "&")
    xml_src = xml_src.replace("&#xD;", "")
    xml_src = xml_src.replace("&#xA;", "")
    xml_src = xml_src.replace("&#x9;", "")