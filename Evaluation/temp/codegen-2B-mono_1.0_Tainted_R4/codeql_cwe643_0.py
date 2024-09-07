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

    xml_source = request.args.get('xml_src')
    if not xml_source:
        return Response(status=404)

    root_xml = etree.XML(xml_source.encode('utf-8'))

    xpath = request.args.get('xpath')
    if not xpath:
        return Response(status=404)

    return Response(etree.tostring(root_xml.xpath(xpath)[0], encoding='unicode', pretty_print=True), mimetype='text/xml; charset=utf-8')


@