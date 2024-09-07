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

    try:
        xml_src = request.args.get('xml_src')
        xmltree = ET.fromstring(xml_src)
        xml_root = ET.fromstringlist(xml_src.splitlines(True))
        return xmltree
    except Exception as e:
        print('Oops!! Error in parsing the XML. Error message is as follows:', e)
