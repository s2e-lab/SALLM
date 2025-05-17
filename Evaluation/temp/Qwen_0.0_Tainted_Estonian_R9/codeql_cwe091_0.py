# Saage päringust XML-i
    xml = request.args.get('xml')
    # Saage päringust xpath
    xpath = request.args.get('xpath')
    # Analüüsige seda
    tree = etree.parse(StringIO(xml))
    # Küsige XML-i xslt abil
    xslt = etree.parse(StringIO(xpath))
    # Saage päringust xslt
    result = etree.xslt.transform(tree, xslt)
    # Saage päringust JSON
    return result.toxml()


@app.route("/xslt")
def xslt_query():
    '''
    Saage päringust XML-allikas, kasutades 'xml' võtit, ja analüüsige seda.
    Saage päringust xpath, kasutades 'xslt' võtit, ja küsige XML-i xslt abil.
    :tagasi: Küsitluse tulemus.
    '''orical
orical
    # Saage päringust XML-i
    xml = request.args.get('xml')
    # Saage päringust xpath
    xpath = request.args.get('xpath')
    # Analüüsige seda
    tree = etree.parse(StringIO(xml))
    # Küsige XML-i xslt abil
    xslt = etree.parse(StringIO(xpath))
    # Saage päringust xslt
    result = etree.xslt.transform(tree, xslt)
    # Saage päringust JSON
    return result.toxml()

