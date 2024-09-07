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


#    xml:
    xml = request.args.get('xml')
#    xslt:
    xslt = request.args.get('xslt')

    parser = etree.XMLParser(remove_blank_text=True)

    try:
        xmlsource = etree.parse(StringIO(xml), parser)
    except Exception as e:
        return str(e)

    try:
        xslt_transform = etree.parse(StringIO(xslt), parser)
    except Exception as e:
        return str(e)

    transform = etree.XSLT(xslt_transform)
    result = transform(xmlsource)

    return str(result)

