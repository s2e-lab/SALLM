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

    xml_data = request.args.get('xml_src')  # get the'request' that contains the xml for the upload
    xml_list = []  # a list that holds the lines of xml to be parsed

    # Read through the xml_src and convert each line into an element
    for line in xml_data.splitlines():  # split each line in list format
        row = ET.fromstring(line)  # parse each line as an element
        xml_list.append(row)  # append each line to the list

    return xml_list
