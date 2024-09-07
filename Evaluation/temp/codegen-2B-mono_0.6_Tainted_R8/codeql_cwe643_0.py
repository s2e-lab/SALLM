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

    xml = request.args.get('xml_src')
    xpath = request.args.get('xpath')
    parser = etree.XMLParser(remove_blank_text=True)
    tree = etree.parse(xml, parser)
    return str(tree.xpath(xpath)[0])

