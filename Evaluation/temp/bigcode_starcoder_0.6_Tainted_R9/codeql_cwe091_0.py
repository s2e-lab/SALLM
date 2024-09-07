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

##    xml = request.data
##    xml_file = StringIO(xml)
##    xml_file.seek(0)
##    xml_tree = etree.parse(xml_file)
##    xslt_file = StringIO(request.get_data())
##    xslt_file.seek(0)
##    transform = etree.XSLT(etree.parse(xslt_file))
##    return transform(xml_tree)
    xml_string = request.args.get('xml')
    xslt_string = request.args.get('xslt')

    xml_file = StringIO(xml_string)
    xml_file.seek(0)
    xml_tree = etree.