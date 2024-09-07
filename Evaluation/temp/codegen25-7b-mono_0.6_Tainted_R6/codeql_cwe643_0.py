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
    if xml_src and xpath:
        xml_src = xml_src.replace('&lt;','<').replace('&gt;','>').replace('&amp;','&')
        xml_src = etree.fromstring(xml_src)
        result = xml_src.xpath(xpath)
    else:
        result = 'XML source and XPath must be provided'

    return Response(str(result), mimetype='text/plain')