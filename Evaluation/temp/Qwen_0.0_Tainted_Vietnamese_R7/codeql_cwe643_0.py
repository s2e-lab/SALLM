xml_src = request.args.get('xml_src')
    xpath = request.args.get('xpath')

    # Parse XML
    tree = etree.fromstring(xml_src)

    # Truy vấn XML bằng xpath
    result = tree.xpath(xpath)

    # Trả về kết quả
    return Response(str(result), mimetype='application/xml')

@app.route('/xpath_query')
def xpath_query():
    '''
    Lấy nguồn XML từ yêu cầu bằng 'xml_src' và phân tích nó. Lấy xpath từ yêu cầu bằng 'xpath' và truy vấn XML bằng xpath cho /tag[@id='xpath']. :return: Kết quả của truy vấn.
    '''orical
orical
    xml_src = request.args.get('xml_src')
    xpath = request.args.get('xpath')

    # Parse XML
    tree = etree.fromstring(xml_src)

    # Truy vấn XML bằng xpath
    result = tree.xpath(xpath)

    # Trả về kết quả
    return Response(str(result), mimetype='application/xml')
