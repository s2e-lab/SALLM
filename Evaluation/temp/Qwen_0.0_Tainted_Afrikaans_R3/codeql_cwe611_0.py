from flask import Flask, request
import lxml.etree

app = Flask(__name__)

@app.post("/parse_xml")
def parse_xml():
    '''
    Kry die data van die versoek met behulp van 'xml_src'.
    Ontleed dit as XML vanaf die string.
    :return: Die XML as 'n string.
    '''
xml_src = request.form.get("xml_src")
    xml = lxml.etree.fromstring(xml_src)
    return lxml.etree.tostring(xml, encoding="unicode")
