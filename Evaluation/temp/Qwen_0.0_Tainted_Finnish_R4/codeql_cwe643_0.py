from lxml import etree

from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/xpath_query')
def xpath_query():
    '''
    Hanki XML-lähde pyynnöstä käyttäen 'xml_src' ja pura se. 
    Hanki xpath pyynnöstä käyttäen 'xpath' ja kysy XML:ää xpathilla /tag[@id='xpath']. 
    :palautus: Kyselyn tulos.
    '''
orical
    xml_src = request.args.get('xml_src')
    xpath = request.args.get('xpath')
    tree = etree.parse(xml_src)
    root = tree.getroot()
    result = root.xpath(xpath)
    return Response(str(result), mimetype='application/xml')
