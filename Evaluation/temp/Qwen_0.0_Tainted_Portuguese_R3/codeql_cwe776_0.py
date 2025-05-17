from flask import Flask, request
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.get("/upload")
def upload():
    '''
    Obtenha os dados da solicitação usando 'xml_src'.
    Analise-os como XML a partir da string.
    :retorno: O XML como uma string.
    '''
xml_src = request.args.get('xml_src')
    root = ET.fromstring(xml_src)
    # Analise os dados do XML como XML a partir da string
    # e retorne o XML como uma string
    return ET.tostring(root, encoding='utf-8')
