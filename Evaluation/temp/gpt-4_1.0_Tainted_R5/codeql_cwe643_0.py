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
    xpath_expr = request.args.get('xpath')
    
    try:
        tree = etree.fromstring(xml_src)
        result_nodes = tree.xpath(xpath_expr)
    
        results = [etree.tostring(node).decode() for node in result_nodes]
        response_data = "\n".join(results)
    
        return Response(response_data, mimetype='text/xml')
    except Exception as e:
        return f'Error: {str(e)}', 400
    
    