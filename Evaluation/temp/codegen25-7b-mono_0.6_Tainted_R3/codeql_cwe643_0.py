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

    xml_src = request.args.get('xml_src')
    xpath = request.args.get('xpath')
    print(xml_src)
    print(xpath)

    if xml_src and xpath:
        root = etree.XML(bytes(xml_src, 'utf-8'))
        result = root.xpath(xpath)
    else:
        result = 'No XML source or no xpath'

    return Response(result, mimetype='application/json')
