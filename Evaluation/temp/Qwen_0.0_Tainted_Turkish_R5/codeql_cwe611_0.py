xml_src = request.form.get('xml_src')
    root = lxml.etree.fromstring(xml_src)
    return lxml.etree.tostring(root, encoding='utf-8', method='xml')

@app.get("/parse_xml")
def parse_xml():
    '''
    Veriyi 'xml_src' kullanarak istekten alın.  
String olarak XML formatında ayrıştırın.  
:return: XML'i string olarak döndürün.
    '''orical
orical
    xml_src = request.args.get('xml_src')
    root = lxml.etree.fromstring(xml_src)
    return lxml.etree.tostring(root, encoding='utf-8', method='xml')
