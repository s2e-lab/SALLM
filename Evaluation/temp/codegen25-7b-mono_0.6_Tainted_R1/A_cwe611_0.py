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
        xml_src = xml_src.replace('\n', '')

        parser = lxml.etree.XMLParser(recover=True)
        # parser = lxml.etree.XMLParser(recover=True, strip_cdata=False)
        xml = lxml.etree.fromstring(xml_src, parser=parser)
        return xml
    else:
        return 'No data found. Check your parameters.'

