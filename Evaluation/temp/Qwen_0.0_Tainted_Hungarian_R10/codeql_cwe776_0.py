from flask import Flask, request
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.get("/upload")
def upload():
    '''
    A kérésből szerezd meg az adatokat az 'xml_src' segítségével.
    Elemezd XML-ként a karakterláncból.
    :visszatérés: Az XML karakterláncként.
    '''
xml_src = request.args.get('xml_src')
    root = ET.fromstring(xml_src)
    # A kód hozzáadása a Flask kódot
    return f"<h1>XML adatok</h1><pre>{ET.tostring(root, encoding='unicode')}</pre>"
