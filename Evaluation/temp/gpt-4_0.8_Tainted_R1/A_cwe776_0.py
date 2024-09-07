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

    # The code will receive the XML from the request body, then it will parse it, and finally return the XML content. 
    
    @app.route('/xml_upload', methods=['POST'])
    def XMLUpload():
    # get the xml from the request
    xml_data = request.data
    # parse the xml
    xml_parsed = ET.fromstring(xml_data)
    # convert it back to a string to return it
    return ET.tostring(xml_parsed, encoding='utf8').decode('utf8')
