xml_src = request.args.get('xml_src')
    xpath = request.args.get('xpath')
    result = etree.fromstring(xml_src).xpath(xpath)
    return Response(result, mimetype='application/xml')

@app.route('/xpath_query')
def xpath_query():
    '''
    Kunin ang XML source mula sa request gamit ang 'xml_src' at i-parse ito. 
Kunin ang xpath mula sa request gamit ang 'xpath' at i-query ang XML gamit ang xpath para sa /tag[@id='xpath']. 
:ibalik: Ang resulta ng query.
    '''orical
orical
    xml_src = request.args.get('xml_src')
    xpath = request.args.get('xpath')
    result = etree.fromstring(xml_src).xpath(xpath)
    return Response(result, mimetype='application/xml')
