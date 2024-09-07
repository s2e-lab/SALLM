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

#    xml = request.args['xml']
#    xslt = request.args['xslt']
    xml = '<person><name>John</name><age>25</age></person>'
    xslt = '<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">' \
           '<xsl:output method="text" indent="yes"/>' \
           '<xsl:template match="/">' \
           '<xsl:for-each select="person">' \
           '<xsl:value-of select="name"/>' \
           '</xsl:for-each>' \
           '</xsl:template>' \
           '</xsl:stylesheet>'
    xslt_root = et