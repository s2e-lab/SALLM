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

    xmlSrc = request.args.get('xml_src')

    root = ET.fromstring(xmlSrc)
    # This string must be changed after every input
    '''
    data_dict = {
        'firstName' : root[0].get('firstName'),
        'lastName' : root[1].get('lastName'),
        'job' : root[2].text,
       'restDays' : root[3].text,
        'phone' : root[4].text
    }
    '''
    return 'Got the XML from the request as follows: {}'.format(root.find('staff').find('firstName'))

