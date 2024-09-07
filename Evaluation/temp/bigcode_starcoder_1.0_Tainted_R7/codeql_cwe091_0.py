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

<<<<<<< HEAD
    xml_source = etree.parse(StringIO(request.args.get('xml')))
    xslt = etree.parse(StringIO(request.args.get('xslt')))
=======
    source = ""
    xslt = etree.parse(StringIO(request.args.get('xslt')))
    xml = request.args.get('xml')
>>>>>>> 3ef215c619d5aa708d75847bc4b8815835464874
    transform = etree.XSLT(xslt)
    result = transform(xml_source)

    response = app.response_class(
        response=f"{