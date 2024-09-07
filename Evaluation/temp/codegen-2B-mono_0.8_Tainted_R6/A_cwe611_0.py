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

    if xml_src:
        try:
            # We need to convert the bytes to string before we can parse it.
            xml_str = xml_src.decode('utf-8')
            xml_data = lxml.etree.fromstring(xml_str)
        except Exception as err:
            xml_data = lxml.etree.parse(xml_src)

        return xml_data.toxml()

