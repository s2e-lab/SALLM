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

    # get the source from request data.
    xml = request.form["xml"]
    xpath = request.form["xslt"]

    # parse the source using etree.
    # etree.XMLTreeBuilder used to parse xml in memory, but in case of large data it might take a few minutes.
    xml_source = etree.XML(xml, etree.XMLParser())

    # define the xpath
    doc = xml_source.xpath(xpath)

    # return the response
    return etree.tostring(doc[0], xml_declaration=True, encoding="UTF-8