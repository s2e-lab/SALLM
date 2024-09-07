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

    if not xml_src:
        return Response(response='XML source not found', status=400)

    if not xpath:
        return Response(response='Xpath not found', status=400)

    try:
        xml = etree.fromstring(xml_src)
        result = xml.xpath(xpath)
        return Response(response=str(result), status=200)
    except Exception as e:
        return Response(response=str(e