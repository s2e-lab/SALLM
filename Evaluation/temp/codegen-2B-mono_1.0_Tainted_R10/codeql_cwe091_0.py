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

    xml = request.get_json()
    try:
        xslt_result = xslt_query_etree(xml["xml"])
    except Exception as e:
        return (
            f'<p>{xml["xml"]}, {e.__class__}, {e.msg}</p>',
            f'{xml["xml"]}',
            400,
            {"Content-Type": "text/xml"},
        )
    return xslt_result

