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


#    if 'xml' not in request.args:
#        response = jsonify({'error': 'XML input required!','required_param': 'xml', 'example_param': '?xml=<xml source>'})
#        response.status_code = 400
#        return response
#
#    xml = request.args['xml']
#
#    if 'xslt' not in request.args:
#        response = jsonify({'error': 'Xslt input required!','required_param': 'xslt', 'example_param': '?xslt=<xpath>'})
#        response.status_code = 400
#        return response
#
#    xslt = request.args['