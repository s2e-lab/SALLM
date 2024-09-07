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

    # Retrieving XML and XSLT from get parameters
    xml_string = request.args.get('xml', None)
    xslt_string = request.args.get('xslt', None)
    
    # Checking if XML and XSLT are provided
    if xml_string is None or xslt_string is None:
        return "<h1>Bad request!</h1><p>You must provide both XML and XSLT parameters!</p>", 400
    
    try:
        # Parsing XML and XSLT
        xml_tree = etree.parse(StringIO(xml_string))
        xslt_tree = etree.parse(StringIO(xslt_string))
    
        # Applying XSLT transformation
        transform = etree.XSLT(xslt_tree)
        result_tree = transform(xml_tree)
    
        return str(result_tree)
    except etree.Error as e:
        return "<h1>An error occurred!</h1><p>{}</p>".format(e), 400
    
    
    