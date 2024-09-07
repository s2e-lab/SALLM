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

    xml = request.args.get('xml')  # get XML source from request
    xslt = request.args.get('xslt')  # get xpath from request
    
    # create an ElementTree object from the XML source
    tree = etree.parse(StringIO(xml))
    
    # create an XSLT object from the xslt
    transform = etree.XSLT(etree.parse(StringIO(xslt)))
    
    # apply the transformation to the XML source and get the result
    result = transform(tree)
    
    # return the serialized result as a string
    return str(result)
