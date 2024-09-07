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

    xml_src = request.args.get('xml')
    xslt_query = request.args.get('xslt')
    
    # Parse the XML source
    parser = etree.XMLParser()
    xml_tree = etree.parse(StringIO(xml_src), parser=parser)
    
    # Create the XSLT transformer
    transformer = etree.XSLT(etree.parse(StringIO(xslt_query)))
    
    # Apply the transformation
    result_tree = transformer(xml_tree)
    result = str(result_tree)
    
    return result
