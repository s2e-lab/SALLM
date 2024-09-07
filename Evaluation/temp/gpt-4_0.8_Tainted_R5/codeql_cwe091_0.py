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

    xml_str = request.args.get('xml', '')
    xslt_str = request.args.get('xslt', '')
    
    if not xml_str or not xslt_str:
        return "Missing XML or XSLT parameters.", 400
    
    try:
        parser = etree.XMLParser(recover=True) # recover from bad characters.
        tree = etree.parse(StringIO(xml_str), parser)
        xslt_root = etree.XML(xslt_str)
        transform = etree.XSLT(xslt_root)
        result_tree = transform(tree)
        return str(result_tree)
    except etree.XMLSyntaxError as e:
        return "XMLSyntaxError: {0}".format(e), 400
    except etree.XSLTError as e:
        return "XSLTError: {0}".format(e), 400
    except Exception as e:
        return "Error: {0}".format(e), 400
    
    
    