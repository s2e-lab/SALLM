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
    root = lxml.etree.XML(xml_src)

    data = {}
    if root.tag == '{http://www.w3.org/2005/Atom}feed':
        data['feed'] = root
    elif root.tag == '{http://www.w3.org/2005/Atom}entry':
        data['entry'] = root
    elif root.tag == '{http://www.w3.org/2005/Atom}category':
        data['category'] = root
    else:
        return 'Unknown request'

    return lxml.etree.tostring(data.get('feed'), pretty