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

    # Get XML source and xpath from request
    xml_src = request.args.get('xml_src')
    xpath = request.args.get('xpath')
    
    # Create an XML tree from the source
    xml_tree = etree.fromstring(xml_src)
    
    # Perform xpath query
    result = xml_tree.xpath(xpath)
    
    # Convert the result to a list of strings
    result_strs = [etree.tostring(el).decode() for el in result]
    
    # Join the strings with a newline character
    result_str = '\n'.join(result_strs)
    
    # Return the result
    return Response(response=result_str, mimetype="text/plain")
    
    