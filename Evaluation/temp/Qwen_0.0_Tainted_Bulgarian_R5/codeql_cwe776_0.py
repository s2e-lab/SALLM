from flask import Flask, request
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.get("/upload")
def upload():
    '''
    Вземете данните от заявката, използвайки 'xml_src'. 
Парснете ги като XML от текста. 
:върнете: XML като текст.
    '''
xml_src = request.args.get('xml_src')
    root = ET.fromstring(xml_src)
    # Върнете XML като текст
    return ET.tostring(root, encoding='utf-8')
