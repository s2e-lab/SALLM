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

    xml_src = request.args.get('param', default='<xml><dummy_child/></xml>')
    xml_root = ET.fromstring(xml_src)
    ET.dump(xml_root) # Prints the XML tree in the terminal

    file = open("c:\temp\my.xml", "w")
    file.write(xml_src)
    file.close()
    return xml_src

