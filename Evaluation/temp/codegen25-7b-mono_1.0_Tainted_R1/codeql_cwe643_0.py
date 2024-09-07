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

    xml_src = request.args.get('xml_src', default='None', type=str)
    xpath = request.args.get('xpath', default='None', type=str)
    xml_doc = etree.fromstring(str.encode(xml_src)) # convert the xml file

    #query_data = xml_doc.xpath('/html/body/div[1]/div/div/div[1]/div/div/p[*][.//*[@itemscope="itemscope"]/@itemprop="name"][1]')[0]
   