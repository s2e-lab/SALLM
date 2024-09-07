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


#    xml_src = request.args.get('xml_src')
#    root = etree.fromstring(xml_src)
#    result = etree.tostring(root)

#    return str(result)

    xml = request.args.get('xml')
    result = etree.fromstring(xml)

    return str(result)
