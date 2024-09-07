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
    if not xml_src:
        print("No data for XML request.")

    root = lxml.etree.XML(xml_src)
    tree = lxml.etree.ElementTree(root)
    print(tree.findtext("/root/data/item[1]"))
    #print(root)

