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
    xml = etree.fromstring(xml)
    result = ''
    if xpath:
        xpath = '//tag[@id="' + xpath + '"]'
        result = etree.tostring(xml.xpath(xpath)[0], encoding='utf-8', method='xml')
    return Response(result, mimetype='text/xml')

