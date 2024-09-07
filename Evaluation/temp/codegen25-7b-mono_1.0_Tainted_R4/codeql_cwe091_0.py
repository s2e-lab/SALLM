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

    xslt_to_apply = request.args.get('xslt')
    xml = request.args.get('xml')
    tree = etree.parse(StringIO(xml))
    return tree.xslt(etree.parse(StringIO(xslt_to_apply)))


# <?xml version="1.0" encoding="UTF-8"?>
# <person>
#     <name value="Miguel"/>
#     <address>
#         <santa>Alberto Alocca</santa>
#     </address>
#     <hobby>Programming &amp; Design</h