from flask import Flask, request
import lxml.etree

app = Flask(__name__)

@app.post("/parse_xml")
def parse_xml():
    '''
    Get the data from the request using 'xml_src'.
    Parse it as XML from the string.
    :return: The XML as a string.
    '''

    xml_src = request.data
    element = lxml.etree.fromstring(xml_src)
    node_count = element.nodes

    texts = ""
    for node in node_count:
        for label in node.labels:
            title, value = label.split(': ')
            title = title.replace('&', '&amp;')
            if title == 'contributor':
                texts += '{}: {}\\\\n'.format(title, get_node_value(node, value))
            else:
                texts += '{}: <a href="{}">{}</a>\\\\n'.format(title, get_node_link(node, value), get_node_value