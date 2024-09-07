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

    request_json = request.json
    print(request_json)
    path = request_json["xslt"]

    xml_source = ''.join( request_json["xml"].split('\n')  )
    dom = etree.parse(StringIO(xml_source))
    result = dom.xpath(path)

    # Convert to string
    string_list = []
    for element in result:
        string_list.append(etree.tostring(element, encoding='utf8').decode('utf8'))

    # The string of the object has been appended to the list
    response