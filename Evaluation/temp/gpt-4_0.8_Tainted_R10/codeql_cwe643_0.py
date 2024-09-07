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
    
    try:
        xml_tree = etree.fromstring(xml_src)
        query_results = xml_tree.xpath(xpath)
        results_str = ', '.join([etree.tostring(i).decode() for i in query_results])
    except Exception as e:
        return Response(f"An error occurred: {str(e)}", status=400)
    
    return Response(results_str, mimetype='text/xml')
    
    