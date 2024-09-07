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
    
    if not xml_src or not xpath:
        return Response('Bad Request', status=400)
    
    try:
        tree = etree.fromstring(xml_src)
        results = tree.xpath(xpath)
        return Response(etree.tostring(results[0]), mimetype='text/xml') if results else ''
    except Exception as e:
        return Response(str(e), status=400)
    
    
    