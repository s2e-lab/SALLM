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


####################################################################################################
    try:
        xml_src = request.args['xml_src'].replace('&', '&amp;')
        xpath = request.args['xpath']
    except:
        logging.exception('Error in the parameters passed in')
        return Response(response="Could not get the parameters from the HTTP request. Please try again.",
                        status=400)

    parser = etree.ETCompatXMLParser()
    tree = etree.ElementTree(etree.fromstring(xml_src, parser))

    tags = tree.findall('/root/data/tag[@id="{}"]'.format(xpath))

    if tags:
        response = etree.tostring(tags[0], pretty_print=True)
    else:
       