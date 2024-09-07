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
    tree = ET.parse(xml_src)
    root = tree.getroot()
    # Create an XML file to return
    xml_tree = ET.Element('data')
    # Get the first level of the XML.
    # The first level we have is the 'session' tag.
    # That tag will have the sessionID, the userID and the groupID.
    session_list = root.findall('session')
    for session_tag in session_list:
        ID = session_tag.attrib['sessionID']
        user_ID = session_tag.attrib['userID']
        group_ID = session_tag.att