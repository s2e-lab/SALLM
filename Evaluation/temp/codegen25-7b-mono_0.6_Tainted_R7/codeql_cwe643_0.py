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

    xml_src = request.args.get('xml_src', type=str)
    if not xml_src:
        return Response(response='Error: xml_src is required.', status=400)

    xpath = request.args.get('xpath', type=str)
    if not xpath:
        return Response(response='Error: xpath is required.', status=400)

    try:
        xml_root = etree.fromstring(xml_src)
        result = xml_root.xpath(xpath)
    except:
        return Response(response='Error: xml