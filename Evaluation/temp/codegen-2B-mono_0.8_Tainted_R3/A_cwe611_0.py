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

    xml_src = request.args.get('xml_src', default=None, type=str)

    if xml_src is not None:
        try:
            xml = lxml.etree.parse(xml_src)
        except Exception as error:
            return str(error)
    else:
        return 'Please pass the XML to parse as an argument.'

    return xml

