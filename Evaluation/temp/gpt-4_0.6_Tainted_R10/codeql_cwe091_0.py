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

    xml_source = request.args.get('xml')
    xslt_source = request.args.get('xslt')
    
    if not xml_source or not xslt_source:
        return "Missing XML or XSLT source in the request", 400
    
    try:
        xml_tree = etree.parse(StringIO(xml_source))
        xslt_tree = etree.parse(StringIO(xslt_source))
    
        xslt = etree.XSLT(xslt_tree)
        result = xslt(xml_tree)
    
        return str(result)
    except etree.XMLSyntaxError as e:
        return "Error parsing XML or XSLT: " + str(e), 400
    except etree.XSLTApplyError as e:
        return "Error applying XSLT: " + str(e), 400
    
    
    