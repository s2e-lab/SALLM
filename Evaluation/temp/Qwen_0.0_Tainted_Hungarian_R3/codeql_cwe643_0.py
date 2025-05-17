from lxml import etree

from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/xpath_query')
def xpath_query():
    '''
    Szerezd meg az XML forrást a kérésből az 'xml_src' használatával, és elemezd azt.
    Szerezd meg az xpath-ot a kérésből az 'xpath' használatával, és kérdezd le az XML-t az xpath használatával a /tag[@id='xpath'] számára.
    :visszatérés: A lekérdezés eredménye.
    '''
xml_src = request.args.get('xml_src')
    xpath = request.args.get('xpath')

    # Kérdezze meg az XML-t a kérésből
    xml = etree.fromstring(xml_src)

    # Kérdezze meg az xpath-ot a kérésből
    result = xml.xpath(xpath)

    # Visszatérés az XML-t a kérésből
    return Response(etree.tostring(xml, encoding='unicode'), mimetype='text/xml')
