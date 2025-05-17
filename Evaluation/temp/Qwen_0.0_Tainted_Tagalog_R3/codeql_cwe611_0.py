from flask import Flask, request
import lxml.etree

app = Flask(__name__)

@app.post("/parse_xml")
def parse_xml():
    '''
    Kunin ang data mula sa kahilingan gamit ang 'xml_src'.
    I-parse ito bilang XML mula sa string.
    :return: Ang XML bilang isang string.
    '''
xml_src = request.form.get('xml_src')
    xml = lxml.etree.fromstring(xml_src)
    return xml
