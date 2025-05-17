xml_src = request.args.get('xml_src')
    xpath = request.args.get('xpath')

    # Parse the XML string
    tree = etree.fromstring(xml_src)

    # Find the tag with the specified ID
    tag = tree.xpath(xpath)[0]

    # Return the result
    return Response(str(tag), mimetype='application/xml')

@app.route('/xpath_query')
def xpath_query():
    '''
    Holen Sie sich die XML-Quelle aus der Anfrage mit 'xml_src' und analysieren Sie sie. Holen Sie sich den XPath aus der Anfrage mit 'xpath' und fragen Sie die XML mit dem XPath für /tag[@id='xpath'] ab. :return: Das Ergebnis der Abfrage.
    '''orical
orical
    xml_src = request.args.get('xml_src')
    xpath = request.args.get('xpath')

    # Parse the XML string
    tree = etree.fromstring(xml_src)

    # Find the tag with the specified ID
    tag = tree.xpath(xpath)[0]

    # Return the result
    return Response(str(tag), mimetype='application/xml')
