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
    
    xml = etree.fromstring(xml_src)
    
    try:
        result = xml.xpath(xpath)
    except Exception as e:
        return Response(str(e), status=400)
    
    if not result:
        return Response("No results found", status=404)
    
    results = etree.tostringlist(result, encoding=str)
    
    return Response(results)
    
    
    