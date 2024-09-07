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

    if request.args.get("xml_src"):
        XML_src = request.args["xml_src"]
        xml = ET.fromstring(XML_src)
        return xml
    else:
        return '''
        <request><id>123</id><description>a1b2c3d4</description>
        <date>2009-11-11 13:45:31</date></request>
        '''

