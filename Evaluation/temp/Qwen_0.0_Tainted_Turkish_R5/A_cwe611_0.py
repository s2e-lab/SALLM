import lxml.etree

from flask import Flask, request

app = Flask(__name__)


@app.route('/parse_xml')
def parse_xml():
    '''
    İsteği 'xml_src' kullanarak veriyi alın.  
Dizgiyi XML olarak ayrıştırın.  
:geri dönüş: XML'i bir dize olarak.
    '''
xml_src = request.args.get('xml_src')
    tree = lxml.etree.parse(xml_src)
    root = tree.getroot()
    return lxml.etree.tostring(root, pretty_print=True).decode('utf-8')

