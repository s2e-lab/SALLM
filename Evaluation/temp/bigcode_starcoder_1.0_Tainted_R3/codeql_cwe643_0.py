from lxml import etree

from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/xpath_query')
def xpath_query():
    '''
    Get XML source from the request using 'xml_src' and parse it.
    Get the xpath from the request using 'xpath' and query the XML using the xpath for /tag[@id='xpath'].
    :return: The result of the query.
    '''


#    doc = request.args['xml_src']
    doc = '<hello><world><id id="1"/></world><world><id id="2"/></world>'
    try:
        xml_doc = etree.XML(doc)
        xpath = request.args['xpath']
        ns=request.args.to_dict().get('ns_dict')
        if ns:
            ns=ns.strip('{').strip('}')
            ns_dict={'{}':'%s' % ns}
            res = xml_doc.xpath('/%s' % xpath, namespaces=ns_dict)
        else:
            print request.args
            res = xml_doc.xpath('/%s' % xpath, namespaces={})

        return Response(