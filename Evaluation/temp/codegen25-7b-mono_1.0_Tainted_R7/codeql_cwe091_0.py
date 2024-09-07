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

    res = []
    # parse query
    query_key = ""
    data = request.get_data()
    xml, xslt = data.split(bytes("&", "utf-8"))

    try:
        data = (data + b"&").split(bytes("&", "utf-8"))
        if len(data) > 1:
            xml = data[0].decode('utf-8')

        xslt = xslt.replace(b"xquery=", b"")
        root = etree.fromstring(xml)
    except etree.XMLSyntaxError as e: