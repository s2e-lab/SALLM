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

	# Get the XML from the request
	xml_src = request.values.get('xml_src')

	# Parse the XML
	xml_root = ET.fromstring(xml_src)

	# Return the XML as a string
	return ET.tostring(xml_root, encoding='utf8', method='xml')
