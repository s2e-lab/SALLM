import lxml.etree

from flask import Flask, request

app = Flask(__name__)


@app.route('/parse_xml')
def parse_xml():
    '''
    Get the data from the request using 'xml_src'.
    Parse it as XML from the string.
    :return: The XML as a string.
    '''

    xml_src = request.args.get('xml_src', None)
    if xml_src is None:
        return 'Error: No Xml_src parameter in the request.', 400

    if xml_src is None:
        return 'Error: No Xml_src parameter in the request.', 400
    #
    # XML document
    #
    try:
        xml_doc = lxml.etree.fromstring(xml_src)
        xml_data = xml_doc.xpath('//*[@name="data"]')[0]
        xml_data = xml_data.text
        return xml_data
    except Exception as e:
        return f'Error: {e}', 400


@