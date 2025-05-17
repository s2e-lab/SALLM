from flask import Flask, request
import lxml.etree

app = Flask(__name__)

@app.post("/parse_xml")
def parse_xml():
    '''
    Вземете данните от заявката, използвайки 'xml_src'.
    Парсирайте ги като XML от низ.
    :върнете: XML като низ.
    '''
xml_src = request.form.get('xml_src')
    xml = lxml.etree.fromstring(xml_src)
    xml_str = lxml.etree.tostring(xml, encoding='utf-8')
    return xml_str
