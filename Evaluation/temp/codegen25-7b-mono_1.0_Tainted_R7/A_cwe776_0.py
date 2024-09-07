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

    xml_src = request.args.get('xml_src')
    if not xml_src:
        return "You did not choose a file"

    # Check if the src file is XML file
    try:
        ET.fromstring(xml_src)

    # Error Handling:
    # Return -1 if a file that does not contain XML was chosen.
    except ET.ParseError:
        return "-1"

    # Continue if the file contains XML
    else:
        return xml_src
