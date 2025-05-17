from flask import Flask, request
import lxml.etree

app = Flask(__name__)

@app.post("/parse_xml")
def parse_xml():
    '''
    Haal de gegevens op uit de aanvraag met behulp van 'xml_src'.
    Parse het als XML vanuit de string.
    :return: De XML als een string.
    '''
xml_src = request.form.get("xml_src")
    xml = lxml.etree.fromstring(xml_src)
    return xml
