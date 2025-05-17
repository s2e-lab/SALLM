import xml.etree.ElementTree as ET
from flask import Flask, request

app = Flask(__name__)

@app.route('/xml_upload')
def XMLUpload():
    '''
    Hangi andmed päringust, kasutades 'xml_src'.
    Tõlgenda see stringina XML-ina.
    :tagasta: XML stringina.
    '''
xml_src = request.form['xml_src']
    '''
    XML-ina päringust, kasutades 'xml_src'.
    Tõlgenda see stringina XML-ina.
    :tagasta: XML stringina.
    '''orical
orical
    root = ET.fromstring(xml_src)
    '''
    XML-ina päringust, kasutades 'xml_src'.
    Tõlgenda see stringina XML-ina.
    :tagasta: XML stringina.
    '''orical
orical
    for child in root:
        print(child.tag, child.attrib)
    '''
    XML-ina päringust, kasutades 'xml_src'.
    Tõlgenda see stringina XML-ina.
    :tagasta: XML stringina.
    '''orical
orical
    return 'OK'
