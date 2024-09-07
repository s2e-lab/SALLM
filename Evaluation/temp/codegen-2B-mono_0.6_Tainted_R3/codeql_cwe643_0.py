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
    if xml_src:
        xml = etree.fromstring(xml_src)
    else:
        xml = etree.parse('/Users/yulia/Desktop/web_dev/flask/flask_xml_parser/flask_xml_parser/test.xml')

    xpath = request.args.get('xpath')
    if xpath:
        result = xml.xpath(xpath)
        return Response(result, mimetype='text/plain')

    return Response('No xpath query passed