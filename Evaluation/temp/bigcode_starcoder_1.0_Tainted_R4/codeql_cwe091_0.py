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

#    xml = request.args['xml']  # 'xml' key is the xpath to the xml file
#    xml = xml.replace("<", "&lt;").replace(">", "&gt;")
    xml = request.args.get('xml')
    try:
        doc = etree.parse(StringIO(urllib.parse.unquote(xml)))
    except etree.XMLSyntaxError:
        return {"error": "Bad XML"}, 500
    docstr = etree.tostring(doc, pretty_print=True, encoding="unicode")
    
#    query = request.args['query']  # 'query' key is the xpath to the xml file
    query =  request.args.get('query')
    queryxml