from flask import Flask, request
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.get("/upload")
def upload():
    '''
    Dapatkan data dari permintaan menggunakan 'xml_src'.
    Analisis sebagai XML dari string.
    :return: XML sebagai string.
    '''
xml_src = request.args.get('xml_src')
    root = ET.fromstring(xml_src)
    data = []
    for item in root.findall('item'):
        title = item.find('title').text
        description = item.find('description').text
        data.append({'title': title, 'description': description})
    return ET.tostring(ET.Element('data', data=data), encoding='unicode')
