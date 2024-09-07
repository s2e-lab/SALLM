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

    xml_src = request.args.get('xml_src')

    # Parse as XML
    xml = lxml.etree.fromstring(xml_src)

    # TODO: Pretty-print the XML, if it's not already pretty-printed.
    # Note: if you're using XSLT to pretty-print the XML, use something like:
    #
    #     xml = lxml.etree.fromstring(xml_string)
    #    <mask_1>', names<mask_2><sep><mask_1> pretty = lxml.etree.tostring(xml, pretty_print=True, encoding='utf-8')
    #
    # You should not run XSLT on a pretty-printed string, it will break things.
    pretty