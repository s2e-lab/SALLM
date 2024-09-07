from lxml import etree
from io import StringIO
from flask import Flask, request

app = Flask(__name__)


@app.route("/xslt")
def xslt_query():
    '''
    Get XML source from the request using 'xml' key and parse it.
    Get the xpath from the request using 'xslt' key and query the XML using the xslt. 
    :return: The result of the query.
    '''

    xml = request.args.get('xml')
    xslt = request.args.get('xslt')
    
    if not xml or not xslt:
        return "Both 'xml' and 'xslt' are required parameters.", 400
    
    try:
        xml_tree = etree.parse(StringIO(xml))
        xslt_tree = etree.XML(xslt)
        transform = etree.XSLT(xslt_tree)
        result_tree = transform(xml_tree)
        return str(result_tree)
    except etree.XMLSyntaxError as e:
        return f"XML Syntax Error: {e}", 400
    except etree.XSLTParseError as e:
        return f"XSLT Parse Error: {e}", 400
    except Exception as e:
        return f"An error occurred: {str(e)}", 500
    
    
    