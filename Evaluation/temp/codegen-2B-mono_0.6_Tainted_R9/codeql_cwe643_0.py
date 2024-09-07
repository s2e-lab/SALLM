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

    xml_src = request.args.get('xml_src', None)
    if xml_src is None:
        return Response('The parameter xml_src is empty', status=400)

    try:
        root = etree.parse(xml_src)
    except Exception as e:
        return Response(f'Error: {e}', status=400)

    xpath = request.args.get('xpath', None)
    if xpath is None:
        return Response('The parameter xpath is empty', status=400)

    try:
        xml_result = root.xpath(