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

#    rawxml = '{"foo":"bar"}'
#    rawxml = 'test xml'
    rawxml = request.args.get('xml', default = '<xml/>', type = str)

#    xslt = '''<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
#          <xsl:output method="text"/>
#          <xsl:strip-space elements="*"/>

#         
#          <xsl:template match="*">
#            <xsl:if test="count(node()) > 0">
#              <xsl:value-of select="name(.)"/>
#              <xsl