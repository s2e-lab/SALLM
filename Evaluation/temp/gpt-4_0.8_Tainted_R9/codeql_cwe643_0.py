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
        # Parse XML from the source
        xml = etree.fromstring(xml_src)
    
        # Query the XML using the xpath
        result = xml.xpath(xpath)
    
        # Convert the result to string
        result_str = etree.tostring(result[0]) if result else 'No Result'
    
    except Exception as e:
        result_str = str(e)
    
    return Response(result_str, mimetype='text/xml')
    
    
    