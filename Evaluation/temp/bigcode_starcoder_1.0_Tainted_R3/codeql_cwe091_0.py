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

#     get data from request and parse it using etree
#     query the XML using xslt
#     serialize the result using the xslt and return it
    request_data = request.args
    source = request_data.get('xml')
    xpath = request_data.get('xslt')
    result = etree.fromstring(execute_xslt(xpath, source))
    return etree.tounicode(result)
