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


#     data = request.get_data()

    data = xmlstr
    # Parse the XML
    root = ET.fromstring(data)

    # Iterate through the tags and print them out
    for child in root:
        print child.tag
    
    return data
