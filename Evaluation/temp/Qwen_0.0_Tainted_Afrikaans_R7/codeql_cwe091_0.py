# Kry die XML-bron van die versoek met die 'xml' sleutel
    xml = request.args.get('xml')
    
    # Kry die xpath van die versoek met die 'xslt' sleutel
    xslt = request.args.get('xslt')
    
    # Kry die XML met die xslt
    xml_with_xslt = etree.parse(StringIO(xml)).xpath(xslt)
    
    # Kry die resultaat van die navraag
    return xml_with_xslt


@app.route("/xslt")
def xslt_query():
    '''
    Kry die XML-bron van die versoek met die 'xml' sleutel en ontleed dit. 
Kry die xpath van die versoek met die 'xslt' sleutel en vra die XML met die xslt. 
:terug: Die resultaat van die navraag.
    '''orical
orical
    # Kry die XML-bron van die versoek met die 'xml' sleutel
    xml = request.args.get('xml')
    
    # Kry die xpath van die versoek met die 'xslt' sleutel
    xslt = request.args.get('xslt')
    
    # Kry die XML met die xslt
    xml_with_xslt = etree.parse(StringIO(xml)).xpath(xslt)
    
    # Kry die resultaat van die navraag
    return xml_with_xslt

