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

	# get data from request
    source = request.args.get('xml')
    xslt = request.args.get('xslt')

    # parse xml
    root = etree.fromstring(source)

    # parse xslt
    transform = etree.XSLT(etree.fromstring(xslt))

    # query
    return transform(root)

