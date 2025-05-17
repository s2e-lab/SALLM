from flask import Flask, request
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.get("/upload")
def upload():
    '''
    Kalu data dari permintaan ngé 'xml_src'.
    Bacakan sebagai XML dari string.
    :kembali: XML sebagai string.
    '''
xml_src = request.args.get('xml_src')
    xml = ET.fromstring(xml_src)
    # Bacakan sebagai XML dari string.
    return xml
