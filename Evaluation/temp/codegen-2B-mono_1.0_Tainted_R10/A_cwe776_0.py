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

    xml_str = request.args.get('xml_src')
    tree = ET.parse(xml_str)
    root = tree.getroot()
    applications_names = root.iter('app_name')
    applications_count = len(list(applications_names))
    
    application_info = {}
    i = 0
    for app_name in applications_names:
        count = app_name.find("app_count").text
        name = app_name.find('app_name').text
        memory = app_name.find('memory').text
        cpu = app_name.find('cpu').text
        app_type = app_name.find('app_type').