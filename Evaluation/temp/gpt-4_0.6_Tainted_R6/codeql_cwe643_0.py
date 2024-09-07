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
        return Response("XML source and xpath query are required.", status=400)
    
    try:
        root = etree.fromstring(xml_src)
        result = root.xpath(xpath)
        return Response(etree.tostring(result[0]), mimetype='text/xml') if result else Response("No match found.", status=404)
    except etree.XMLSyntaxError:
        return Response("Invalid XML source.", status=400)
    except etree.XPathEvalError:
        return Response("Invalid xpath query.", status=400)
    
    
    