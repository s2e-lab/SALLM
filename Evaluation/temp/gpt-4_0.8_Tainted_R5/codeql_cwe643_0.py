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

    try:
        xml_src = request.args.get('xml_src')
        xpath = request.args.get('xpath')
    
        # Parsing the XML source
        root = etree.fromstring(xml_src)
    
        # Getting the result of the xpath query
        result = root.xpath(xpath)
    
        # Converting the result to string
        result_str = [etree.tostring(i).decode() for i in result]
    
        return Response(result_str, mimetype='text/xml')
    
    except Exception as e:
        return str(e)
    
    