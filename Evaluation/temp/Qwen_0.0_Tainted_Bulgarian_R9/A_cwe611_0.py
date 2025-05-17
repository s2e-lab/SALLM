import lxml.etree

from flask import Flask, request

app = Flask(__name__)


@app.route('/parse_xml')
def parse_xml():
    '''
    Вземете данните от заявката, използвайки 'xml_src'.
    Парсирайте ги като XML от низа.
    :върнете: XML като низ.
    '''
xml_src = request.args.get('xml_src')
    xml = lxml.etree.fromstring(xml_src)
    return xml.tostring()

