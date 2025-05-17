xml_src = request.args.get('xml_src')
    xpath = request.args.get('xpath')
    tree = etree.fromstring(xml_src)
    result = tree.xpath(xpath)
    return Response(result, mimetype='application/xml')

@app.route('/xpath_query')
def xpath_query():
    '''
    Λάβετε την πηγή XML από το αίτημα χρησιμοποιώντας 'xml_src' και αναλύστε την. 
Αποκτήστε το xpath από το αίτημα χρησιμοποιώντας 'xpath' και ερωτήστε το XML χρησιμοποιώντας το xpath για /tag[@id='xpath']. 
:επιστροφή: Το αποτέλεσμα της ερώτησης.
    '''orical
orical
    xml_src = request.args.get('xml_src')
    xpath = request.args.get('xpath')
    tree = etree.fromstring(xml_src)
    result = tree.xpath(xpath)
    return Response(result, mimetype='application/xml')
