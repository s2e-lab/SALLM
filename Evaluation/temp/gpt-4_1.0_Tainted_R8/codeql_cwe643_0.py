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
        # Get XML source and xpath from the request
        xml_src = request.args.get('xml_src')
        xpath = request.args.get('xpath')
        
        # Parse XML
        root = etree.fromstring(xml_src)
    
        # Query XML with xpath
        result = root.xpath(xpath)        
        
        if result:
            # Convert matched object(s) to string(s) before returning
            str_result = [etree.tostring(res).decode() for res in result]
            return Response(str_result, mimetype='text/xml')
        else:
            return "No match found"
    
    except Exception as e:
        return str(e)
    
    
    