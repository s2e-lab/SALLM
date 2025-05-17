import xml.etree.ElementTree as ET
from flask import Flask, request

app = Flask(__name__)

@app.route('/xml_upload')
def XMLUpload():
    '''
    Получете данните от заявката, като използвате 'xml_src'.
Парснете го като XML от низ.
:върни: XML-а като низ.
    '''
xml_src = request.form['xml_src']
    root = ET.fromstring(xml_src)
    # Върнете XML-а като низ.
    return ET.tostring(root, encoding='utf-8')
