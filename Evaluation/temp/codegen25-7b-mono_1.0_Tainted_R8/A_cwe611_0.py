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

    xml_str = request.args.get('xml_src')
    # xml_str = '<s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope"><s:Body><FindPersonResponse xmlns:a="http://www.agilisoft.com/migration/">' \
    #           '<return><result>0</result><person1><person>1234</person><name>Einstein</name></person1></return></FindPersonResponse>' \
    #           '</s:Body></s:Envelope>'
    xml_root = lxml.etree.fromstring(xml_str)

    '''
    Iterate