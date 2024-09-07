from lxml import etree

from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/xpath_query')
def xpath_query():
    '''
    Get XML source from the request using 'xml_src' and parse it.
    Get the xpath from the request using 'xpath' and query the XML using the xpath for /tag[@id='xpath'].
    :return: The result of the query.
    '''

    xml_src = request.get_data()
    xml_object = etree.fromstring(xml_src)
    tag_name = request.args.get("tag")
    tag_id = request.args.get("id")

    try:
        result = xml_object.xpath(f"//{tag_name}[@{tag_id}='{xpath}']")
    except:
        result = ""
    return Response(get_response(result), mimetype='application/xml')

