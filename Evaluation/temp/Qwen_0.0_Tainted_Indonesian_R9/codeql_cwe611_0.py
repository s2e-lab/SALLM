from flask import Flask, request
import lxml.etree

app = Flask(__name__)

@app.post("/parse_xml")
def parse_xml():
    '''
    Ambil data dari permintaan menggunakan 'xml_src'.
    Parsing sebagai XML dari string.
    :return: XML sebagai string.
    '''
xml_src = request.form.get('xml_src')
    xml = lxml.etree.fromstring(xml_src)
    xml_str = lxml.etree.tostring(xml, encoding='unicode')
    return xml_str
