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

    xml_src = request.args["xml_src"]

    xml_string = ET.fromstring(xml_src)

    '''
    In the code below, we are iterating over the XML tree and extracting the 
    data of interest.
    '''

    root = xml_string.find('root')

    if root is None:
        return "No root tag found"

    device_type = root.find('deviceType')

    if device_type is None:
        return "No deviceType tag found"

    name = device_type.find('name')

    if name is None:
        return "No name tag found"

    serial_number = device_type.find('serialNumber')

    if serial_number