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
        return "XML source and XSLT query are required."
    
    try:
        # Parse XML and XSLT
        xml_parser = etree.XMLParser(remove_blank_text=True)
        xml_tree = etree.parse(StringIO(xml), xml_parser)
        xslt_tree = etree.parse(StringIO(xslt), xml_parser)
    
        # Transform XML with the XSLT
        transform = etree.XSLT(xslt_tree)
        result_tree = transform(xml_tree)
    
        return str(result_tree)
    
    except Exception as e:
        return f"Error: {str(e)}"
    
    
    