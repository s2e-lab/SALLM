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
        xml_file = xml_src.replace("[&lt;","<").replace("&gt;]",">").replace("&lt;","<").replace("&gt;",">")
        xml = ET.fromstring(xml_file)
        root = ET.tostring(xml)
        return root
    except Exception as e:
        print("Exception: ", e)
        print("Error code:-1")
        quit(0)
