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

    xml_src = request.args.get('xml_src', '')
    xpath = request.args.get('xpath', '')
    
    try:
        root = etree.fromstring(xml_src)
        result = root.xpath(xpath)
        result_text = etree.tostring(result[0]) if result else 'No results'
    except etree.XMLSyntaxError:
        result_text = 'Invalid XML'
    except etree.XPathEvalError:
        result_text = 'Invalid XPath'
    
    return Response(result_text, mimetype='text/xml')
    
    