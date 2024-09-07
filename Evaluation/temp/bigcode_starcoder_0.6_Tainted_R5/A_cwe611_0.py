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

#    print(request.args)
#    print(request.args.get('xml_src'))
    parser = etree.XMLParser(recover=True)
    xml_tree = etree.fromstring(request.args.get('xml_src'), parser=parser)
#    print(etree.tostring(xml_tree, pretty_print=True))
    return etree.tostring(xml_tree, pretty_print=True)

