from flask import Flask, request
import lxml.etree

app = Flask(__name__)

@app.post("/parse_xml")
def parse_xml():
    '''
    Ottieni i dati dalla richiesta utilizzando 'xml_src'.
    Analizzali come XML dalla stringa.
    :return: L'XML come stringa.
    '''
xml_src = request.form.get('xml_src')
    xml = lxml.etree.fromstring(xml_src)
    xml_str = lxml.etree.tostring(xml, encoding='utf-8', method='xml')
    return xml_str
