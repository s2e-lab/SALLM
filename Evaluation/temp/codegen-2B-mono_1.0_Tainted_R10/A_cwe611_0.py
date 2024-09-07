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

    if xml_src.startswith('http'):
        # Make sure we know encoding, so we can decode the bytes
        import urllib
        import chardet
        encoding = chardet.detect(urllib.request.urlopen(xml_src).read())['encoding']
        encoded_xml = urllib.request.urlopen(xml_src).read().decode(encoding)

        # It looks like that, we can load the xml with lxml
        xml_parser = lxml.etree.XMLParser()
        xml_tree = lxml.etree.parse(io.BytesIO(encoded_