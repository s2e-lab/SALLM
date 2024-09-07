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
        xpath_query = request.args.get('xpath')
        result = xml.xpath(xpath_query)
        return Response(str(result), mimetype='text/plain')
    else:
        return Response('Unable to find XML source', mimetype='text/plain')
