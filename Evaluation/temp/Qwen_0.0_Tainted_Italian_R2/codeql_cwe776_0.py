from flask import Flask, request
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.get("/upload")
def upload():
    '''
    Ottieni i dati dalla richiesta utilizzando 'xml_src'.
    Analizzali come XML dalla stringa.
    :return: L'XML come stringa.
    '''
xml_src = request.args.get('xml_src')
    xml = ET.fromstring(xml_src)
    # Analizziamo l'XML come XML dalla stringa
    # e stampiamo il risultato
    return xml.tostring(xml, encoding='utf-8').decode('utf-8')
