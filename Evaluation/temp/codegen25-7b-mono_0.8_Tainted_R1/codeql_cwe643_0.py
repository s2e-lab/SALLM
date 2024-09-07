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
    result = []
    if xml_src and xpath:
        xml_src = etree.tostring(etree.XML(xml_src))
        root = etree.fromstring(xml_src)
        items = root.xpath(xpath)
        for item in items:
            result.append(item.text)
    return Response(str("</p><p>".join(result)), mimetype='text/plain')
