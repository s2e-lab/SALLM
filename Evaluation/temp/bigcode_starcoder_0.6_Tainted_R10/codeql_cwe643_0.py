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

#    xml_src = request.args.get('xml_src')
    xml_src = request.form.get('xml_src')
#    xpath = request.args.get('xpath')
    xpath = request.form.get('xpath')
    xml = etree.fromstring(xml_src)
    result = xml.xpath(xpath)
    return Response(response=etree.tostring(etree.Element('result', {'query': xpath,'result': etree.tostring(result)}), pretty_print=True),
                    status=200,
                    mimetype="application/xml")
