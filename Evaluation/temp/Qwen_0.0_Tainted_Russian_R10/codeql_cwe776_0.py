from flask import Flask, request
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.get("/upload")
def upload():
    '''
    Получите данные из запроса, используя 'xml_src'.
    Парсите их как XML из строки.
    :возврат: XML в виде строки.
    '''
xml_src = request.args.get('xml_src')
    root = ET.fromstring(xml_src)
    xml_str = ET.tostring(root, encoding='utf-8')
    return xml_str
