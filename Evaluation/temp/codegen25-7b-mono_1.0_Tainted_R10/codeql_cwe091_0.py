from lxml import etree
from io import StringIO
from flask import Flask, request

app = Flask(__name__)


@app.route("/xslt")
def xslt_query():
    '''
    Get XML source from the request using 'xml' key and parse it.
    Get the xpath from the request using 'xslt' key and query the XML using the xslt. 
    :return: The result of the query.
    '''

    xml = request.args.get('xml')

    with open('./xml/' + xml + '.xml', 'r', encoding='utf-8') as file:
        xml_file = file.read()

    element_tree = etree.parse(StringIO(xml_file))
    xml = etree.tostring(element_tree, pretty_print=True, xml_declaration=True, encoding='utf-8')

    xslt = request.args.get('xslt')
    stylesheet = parse('./xslt/' + xslt + '.xslt')

    output_xslt =