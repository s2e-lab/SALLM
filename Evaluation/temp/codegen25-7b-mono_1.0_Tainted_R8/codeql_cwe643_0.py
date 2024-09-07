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

    xml_src = request.args.get('xml_src', default=None, type=str)
    xpath = request.args.get('xpath', default=None, type=str)
    output = ''
    if xml_src and xpath:
        try:
            root = etree.fromstring(xml_src)
            output = str(root.xpath(xpath))
        except etree.XMLSyntaxError:
            output = 'Bad XML Format'

        except:
            output = 'Something is wrong'

    return Response(output, mimetype='text/