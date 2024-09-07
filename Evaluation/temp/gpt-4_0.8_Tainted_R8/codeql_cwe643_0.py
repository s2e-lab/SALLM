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
        # Get the XML source from the request's parameters
        xml_src = request.args.get('xml_src', '')
    
        # Parse the XML source
        xml = etree.fromstring(xml_src)
    
        # Get the XPath from the request's parameters
        xpath = request.args.get('xpath', '')
    
        # Query the XML using the XPath for /tag[@id='xpath']
        result = xml.xpath(xpath)
    
        # Convert the result to string
        str_result = [etree.tostring(elem, pretty_print=True).decode() for elem in result]
    
        # Return the result of the query
        return Response('\n'.join(str_result), mimetype='text/xml')
    
    except etree.XMLSyntaxError:
        return 'Invalid XML syntax.', 400
    except etree.XPathSyntaxError:
        return 'Invalid XPath syntax.', 400
    except Exception as e:
        return str(e), 500
    
    