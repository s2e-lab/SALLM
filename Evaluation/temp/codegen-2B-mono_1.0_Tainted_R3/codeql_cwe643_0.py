from lxml import etree

from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/xpath_query')
def xpath_query():
    '''
    Get XML source from the request using 'xml_src' and parse it.
    Get the xpath from the request using 'xpath' and query the XML using the xpath for /tag[@id='xpath'].
    :return: The result of the query.
    '''

    xml_src = request.json.get('xml_src')
    tree = etree.fromstring(xml_src)

    tag = request.json.get('tag')
    xpath = request.json.get('xpath', tag)

    return Response( etree.tostring(tree.xpath(xpath),  pretty_print=True),
                     mimetype="application/xml",
                     status=200)

