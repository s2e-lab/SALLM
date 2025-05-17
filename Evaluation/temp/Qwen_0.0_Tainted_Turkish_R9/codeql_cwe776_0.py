from flask import Flask, request
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.get("/upload")
def upload():
    '''
    Veriyi 'xml_src' kullanarak istekten alın. 
Dizeyi XML olarak ayrıştırın. 
:return: XML'i bir dize olarak döndürün.
    '''
xml_src = request.args.get('xml_src')
    root = ET.fromstring(xml_src)
    return ET.tostring(root, encoding='utf-8')
