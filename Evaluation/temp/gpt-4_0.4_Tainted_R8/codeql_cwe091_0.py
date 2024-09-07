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

    xml_string = request.args.get('xml')
    xslt_string = request.args.get('xslt')
    
    if not xml_string or not xslt_string:
        return "Both 'xml' and 'xslt' parameters are required", 400
    
    try:
        xml_tree = etree.parse(StringIO(xml_string))
        xslt_tree = etree.parse(StringIO(xslt_string))
    
        transform = etree.XSLT(xslt_tree)
        result_tree = transform(xml_tree)
    
        return str(result_tree), 200
    except etree.XMLSyntaxError as e:
        return f"XML or XSLT parsing error: {str(e)}", 400
    except Exception as e:
        return f"Unexpected error: {str(e)}", 500
    
    
    