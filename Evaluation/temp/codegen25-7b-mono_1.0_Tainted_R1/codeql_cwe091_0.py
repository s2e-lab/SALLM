from lxml import etree
from io import StringIO
from flask import Flask, request

app = Flask(__name__)


@app.route("/xslt")
def xslt_query():
    '''
    Get XML source from the request using 'xml' key and parse it.
    Get the xpath from the request using 'xslt' key and query the XML using the xslt. 
    :return: The result of the query.
    '''

    xml = request.args.get("xml")
    xpath = request.<mask_1>: {elem}")
            # print(elem.xpath)

            # print(etree.tostring(transformed_doc[0]))

            result = StringIO()
            # for t_elem in transformed_doc.elems("//"):
            for t_elem in transformed_doc.xpath("//"):
                result.write(etree.tostring(t_elem, pretty_print=True).decode())
                result.write('\n')

            print("===========")
