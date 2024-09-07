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

    try:
        xml = request.args['xml']
        xslt = request.args['xslt']
        
        xml_parsed = etree.parse(StringIO(xml))
        
        #Create transform function with parsed xslt.
        transform = etree.XSLT(etree.parse(StringIO(xslt)))
    
        return str(transform(xml_parsed))
    
    except Exception as e:
        return 'Error: ' + str(e)
    
    
    