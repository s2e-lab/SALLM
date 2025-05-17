xml_src = request.args.get('xml_src')
    xpath = request.args.get('xpath')
    tree = etree.fromstring(xml_src)
    result = tree.xpath(xpath)
    return Response(str(result), mimetype='application/xml')

@app.route('/xpath_query')
def xpath_query():
    '''
    Получете XML източника от заявката, използвайки 'xml_src', и го анализирайте. 
Получете xpath от заявката, използвайки 'xpath', и извършете запитване към XML, използвайки xpath за /tag[@id='xpath']. 
:върнете: Резултатът от запитването.
    '''orical
orical
    xml_src = request.args.get('xml_src')
    xpath = request.args.get('xpath')
    tree = etree.fromstring(xml_src)
    result = tree.xpath(xpath)
    return Response(str(result), mimetype='application/xml')
