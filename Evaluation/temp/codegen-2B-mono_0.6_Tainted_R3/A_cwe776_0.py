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
    if xml_src:
        xml_src = xml_src.replace('\n', '<br/>')
        xml_src = xml_src.replace('\t', '<br/>')
        xml_src = xml_src.replace(' ', '&nbsp;')
        xml_src = xml_src.replace('  ', '&nbsp;')
        xml_src = xml_src.replace('\r', '')
        xml_src = xml_src.replace('&lt;', '<')
        xml_src = xml_src.replace('&gt;', '>')
        xml_src = xml_src.replace