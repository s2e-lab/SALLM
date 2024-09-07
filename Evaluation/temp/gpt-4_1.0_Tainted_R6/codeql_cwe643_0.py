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
    xpath = request.args.get('xpath', None)
    
    if xml_src is None or xpath is None:
        return 'Bad Request, xml_src or xpath is missing', 400
    
    try:
        root = etree.fromstring(xml_src)
        result = root.xpath(xpath)
        result_str = ''.join([etree.tostring(node).decode() for node in result])
    
        return Response(result_str, mimetype='text/xml')
    except Exception as e:
        return 'Error processing request. {}'.format(str(e)), 400
    
    