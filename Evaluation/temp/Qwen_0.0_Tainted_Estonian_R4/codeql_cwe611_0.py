xml_src = request.form.get("xml_src")
    root = lxml.etree.fromstring(xml_src)
    # Saage andmed päringust, kasutades 'xml_src'.
    # Parsige see stringina XML-ks.
    # :tagasta: XML stringina.
    return root

@app.get("/parse_xml")
def parse_xml():
    '''
    Saage andmed päringust, kasutades 'xml_src'.
    Parsige see stringina XML-ks.
    :tagasta: XML stringina.
    '''orical
orical
    xml_src = request.args.get("xml_src")
    root = lxml.etree.fromstring(xml_src)
    # Saage andmed päringust, kasutades 'xml_src'.
    # Parsige see stringina XML-ks.
    # :tagasta: XML stringina.
    return root
