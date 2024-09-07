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

    # get xml source and xpath from request
    xml_src = request.args.get('xml_src')
    xpath = request.args.get('xpath')
    
    # parse the xml source
    root = etree.fromstring(xml_src)
    
    # query the xml using the xpath
    result = root.xpath(xpath)
    
    # format the result
    result_str = '\n'.join([etree.tostring(e).decode() for e in result])
    
    return Response(result_str, mimetype='text/plain')
    
    
    