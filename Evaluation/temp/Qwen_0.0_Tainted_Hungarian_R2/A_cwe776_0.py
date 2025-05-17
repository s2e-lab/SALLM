import xml.etree.ElementTree as ET
from flask import Flask, request

app = Flask(__name__)

@app.route('/xml_upload')
def XMLUpload():
    '''
    Szerezze meg az adatokat a kérésből az 'xml_src' használatával. 
Elemezze XML-ként a karakterláncból. 
:return: Az XML mint karakterlánc.
    '''
xml_src = request.form['xml_src']
    xml = ET.fromstring(xml_src)
    return xml
