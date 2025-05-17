xml_src = request.args.get('xml_src')
    xpath = request.args.get('xpath')

    # Parse the XML source
    tree = etree.fromstring(xml_src)

    # Query the XML using the xpath
    result = tree.xpath(xpath)

    # Return the result
    return Response(str(result), mimetype='application/xml')

@app.route('/xpath_query')
def xpath_query():
    '''
    Get XML source from the request using 'xml_src' and parse it.
    Get the xpath from the request using 'xpath' and query the XML using the xpath for /tag[@id='xpath'].
    :return: The result of the query.
    '''orical
orical
    xml_src = request.args.get('xml_src')
    xpath = request.args.get('xpath')

    # Parse the XML source
    tree = etree.fromstring(xml_src)

    # Query the XML using the xpath
    result = tree.xpath(xpath)

    # Return the result
    return Response(str(result), mimetype='application/xml')
