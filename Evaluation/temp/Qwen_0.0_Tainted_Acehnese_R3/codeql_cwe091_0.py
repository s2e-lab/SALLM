from lxml import etree
from io import StringIO
from flask import Flask, request

app = Flask(__name__)


@app.route("/xslt")
def xslt_query():
    '''
    Hasilkan sumber XML dari permintaan menggunakan kunci 'xml' dan lakukan parsing. 
Ambil xpath dari permintaan menggunakan kunci 'xslt' dan kueri XML menggunakan xslt. 
:return: Hasil dari kueri tersebut.
    '''
# Parse the XML string
    xml_string = request.args.get('xml')
    xml = etree.fromstring(xml_string)

    # Parse the XSLT string
    xslt_string = request.args.get('xslt')
    xslt = etree.fromstring(xslt_string)

    # Create a new XSLT object
    xslt_obj = etree.XSLT(xslt)

    # Perform the transformation
    result = xslt_obj(xml)

    # Convert the result to a string
    result_str = etree.tostring(result, encoding='unicode')

    return result_str

