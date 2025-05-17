from lxml import etree

from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/xpath_query')
def xpath_query():
    '''
    Saada XML allikas päringust, kasutades 'xml_src' ja analüüsi see.
    Saada xpath päringust, kasutades 'xpath' ja päring XML-i kaudu xpath'i jaoks /tag[@id='xpath'].
    :return: Päringu tulemus.
    '''
orical
    xml_src = request.args.get('xml_src')
    xpath = request.args.get('xpath')

    # Analüüsi XML-i
    tree = etree.parse(xml_src)
    root = tree.getroot()

    # Analüüsi xpath'i
    xpath_node = root.xpath(xpath)

    # Saada päringus
    response = Response(etree.tostring(root, encoding='unicode'), mimetype='text/xml')
    return response
