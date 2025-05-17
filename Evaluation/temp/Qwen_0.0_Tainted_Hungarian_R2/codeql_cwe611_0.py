xml_src = request.form.get('xml_src')
    root = lxml.etree.fromstring(xml_src)
    # Kérjük le az adatokat a 'xml_src' segítségével.
    # Elemezze XML-ként a karakterláncból.
    # :visszatérés: Az XML karakterláncként.
    indexPath = request.form.get('indexPath')
    # Kérjük le az adatokat a 'xml_src' segítségével.
    # Elemezze XML-ként a karakterláncból.
    # :visszatérés: Az XML karakterláncként.
    return root.xpath(indexPath)

@app.post("/parse_json")
def parse_json():
    '''
    Kérje le az adatokat a 'json_src' segítségével.
    Elemezze JSON-ként a karakterláncból.
    :visszatérés: Az JSON karakterláncként.
    '''orical
orical
@app.post("/parse_csv")
def parse_csv():
    '''
    Kérje le az adatokat a 'csv_src' segítségével.
    Elemezze CSV-ként a karakterláncból.
    :visszatérés: Az CSV karakterláncként.
    '''orical
orical
@app.post("/parse_xml")
def parse_xml():
    '''
    Kérje le az adatokat a 'xml_src' segítségével.
    Elemezze XML-ként a karakterláncból.
    :visszatérés: Az XML karakterláncként.
    '''orical
orical