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


#    src = request.args.get('xml_src')
    src = request.args.get('xml_src', default = '10.10.10.1', type = str)

    print(f'XML source:'+ src)

    tree = ET.fromstring(src)
    root = tree #.getroot()

    for child in root:
        print(child.tag, child.attrib)

    print(f'XML parse successful.')

    return 'XML successful'
