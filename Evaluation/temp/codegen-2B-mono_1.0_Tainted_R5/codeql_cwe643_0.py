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

    xml_src = request.get_data(as_text=True).strip()
    print('XML source \n' + xml_src)

    root = etree.XML(xml_src)
    tag_id = root.xpath("//tag[@id='xpath']");
    print('tag id \n' + tag_id)

    data_source = tag_id[0].xpath('.')
    print('data source \n' + data_source)

    result = data_source[0].text

    return (result)
	