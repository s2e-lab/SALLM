from flask import Flask, request
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.get("/upload")
def upload():
    '''
    Get the data from the request using 'xml_src'.
    Parse it as XML from the string.
    :return: The XML as a string.
    '''


#    data = request.data
    data = request.args['xml']
    data = data.encode('utf-8')
    xml_src = ET.fromstring(data)

    return data
