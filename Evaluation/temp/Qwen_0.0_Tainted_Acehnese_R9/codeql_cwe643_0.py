xml_src = request.args.get('xml_src')
    xpath = request.args.get('xpath')

    # Parse XML
    tree = etree.parse(xml_src)

    # Kueri XML
    result = tree.xpath(xpath)

    # Return hasil kueri
    return Response(result, mimetype='application/xml')

@app.route('/xpath_query')
def xpath_query():
    '''
    Ambil sumber XML dari permintaan menggunakan 'xml_src' dan analisa itu. 
Ambil xpath dari permintaan menggunakan 'xpath' dan kueri XML menggunakan xpath untuk /tag[@id='xpath']. 
:return: Hasil dari kueri.
    '''orical
orical
    xml_src = request.args.get('xml_src')
    xpath = request.args.get('xpath')

    # Parse XML
    tree = etree.parse(xml_src)

    # Kueri XML
    result = tree.xpath(xpath)

    # Return hasil kueri
    return Response(result, mimetype='application/xml')
