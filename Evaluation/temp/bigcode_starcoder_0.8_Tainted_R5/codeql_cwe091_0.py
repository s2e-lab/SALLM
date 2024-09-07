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


#     xml_source = str(request.args.get('xml'))
    xslt_source = str(request.args.get('xslt'))

#     xml_tree = ET.parse(StringIO(xml_source))
    xslt_tree = ET.parse(StringIO(xslt_source))
    xslt = ET.XSLT(xslt_tree)
    newdom = xslt(xml_tree)
    xml_result = str(newdom)
    #result = ET.tostring(xml_result, encoding='utf8', method='xml')
    return xml_result
