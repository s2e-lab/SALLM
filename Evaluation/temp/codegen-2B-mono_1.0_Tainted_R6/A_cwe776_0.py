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

    # Get all the data from the Postman.
    xml_src = request.get_data()
    # Parse the XML data in to a tree.
    data = ET.fromstring(xml_src)
    # XML is returned.
    return str(data)

# -----------------------------------------------    PRINT  ------------------------------------------------