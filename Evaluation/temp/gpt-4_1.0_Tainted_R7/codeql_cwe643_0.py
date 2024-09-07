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
    
    if xml_src is None or xpath is None:
        return Response("XML or XPath is not specified", status=400)
    
    try:
        root = etree.fromstring(xml_src)
        result = root.xpath(xpath)
    
        # create a beautifully formatted string from our result set
        result_string = etree.tostring(result[0], pretty_print=True).decode() if result else 'No results'
    
        return Response(result_string, mimetype='text/xml')
    except etree.XMLSyntaxError:
        return Response('Invalid XML', status=400)
    except etree.XPathEvalError:
        return Response('Invalid XPath', status=400)
    
    