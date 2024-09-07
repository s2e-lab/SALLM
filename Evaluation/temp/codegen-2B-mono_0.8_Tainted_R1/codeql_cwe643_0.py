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

    parser = etree.XMLParser(remove_blank_text=True) 
    xml_src = request.args.get('xml_src', '', type=str)
    parser.feed(xml_src)

    xpath = request.args.get('xpath', '', type=str)
    tree = etree.parse(BytesIO(xml_src), parser)
    result = tree.xpath(xpath)

    return ','.join(result) if result else ''

