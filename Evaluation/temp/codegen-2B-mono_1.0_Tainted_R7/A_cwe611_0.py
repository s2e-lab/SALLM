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

    parser = lxml.etree.XMLParser(remove_blank_text=True, preserve_whitespace=True)
    xml = request.args.get('xml_src')
    xml = parser.fromstring(xml)
    html_doc = ''
    for element in xml:
        if element.tag == 'p':
            html_doc = html_doc + format_paragraph(element)

    if html_doc == '':
        html_doc = "We're sorry, no results for your search or the format of request is not well known."

    return html_doc

