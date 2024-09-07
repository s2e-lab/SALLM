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

    xml_str = request.args['xml']               # get xml source from the request 
    xpath_str = request.args["xslt"]            # get xpath from the request
    tree = etree.parse(StringIO(xml_str))      # parse xml using built in parser 
    root = tree.getroot()

    result_dict = etree.XPath(xpath_str).evaluate(root)
    result = etree.tostring(result_dict, pretty_print=True)
    return result

