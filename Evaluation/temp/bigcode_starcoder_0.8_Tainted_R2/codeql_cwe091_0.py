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


#    try:
    xslt_query = request.args.get("xslt")
    source = request.args.get("xml")
    xmldoc = etree.parse(source)
    transform = etree.XSLT(etree.parse(xslt_query))
    result = transform(xmldoc)
    return str(result)

#    except Exception as e:
#        return "error occured while parsing: " + str(e)


#