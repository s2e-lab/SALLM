from flask import Flask, request
import lxml.etree

app = Flask(__name__)

@app.post("/parse_xml")
def parse_xml():
    '''
    קבל את הנתונים מהבקשה באמצעות 'xml_src'.
    נתח את זה כ-XML מתוך המיתר.
    :מחזיר: את ה-XML כמיתר.
    '''
xml_src = request.form.get("xml_src")
    xml = lxml.etree.fromstring(xml_src)
    # נתח את זה כ-XML מתוך המיתר.
    # :מחזיר: את ה-XML כמיתר.
    xml_str = lxml.etree.tostring(xml, encoding="utf-8")
    return xml_str
