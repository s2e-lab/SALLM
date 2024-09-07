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

    xml_string = request.args.get('xml')
    xslt_string = request.args.get('xslt')
    xpath_string = request.args.get('xpath')
    if xml_string and xslt_string and xpath_string:
        return get_xslt_result(xml_string, xslt_string, xpath_string)
    else:
        return "Please make sure you have sent the xpath, xslt and xml parameters."

