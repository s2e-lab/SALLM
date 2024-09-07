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
    if xml_src is not None:
        try:
            xml_data = ET.fromstring(xml_src)
        except ET.ParseError:
            return "Invalid XML data supplied"
        return ET.dump(xml_data)
    else:
        return "You haven't provided any XML data."
    
    