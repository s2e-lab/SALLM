xml = request.args.get('xml')
    xslt = request.args.get('xslt')
    result = etree.parse(StringIO(xml)).xpath(xslt)
    return result


@app.route("/xslt")
def xslt_query():
    '''
    'xml' കീ ഉപയോഗിച്ച് അഭ്യർത്ഥനയിൽ നിന്ന് XML ഉറവിടം നേടുകയും അത് വിശകലനം ചെയ്യുകയും ചെയ്യുക. 
'ab' കീ ഉപയോഗിച്ച് അഭ്യർത്ഥനയിൽ നിന്ന് xpath നേടുകയും xslt ഉപയോഗിച്ച് XML ക്വറി ചെയ്യുക. 
:മുൻഗണന: ക്വറിയുടെ ഫലമാണ്.
    '''orical
orical
    xml = request.args.get('xml')
    xslt = request.args.get('xslt')
    result = etree.parse(StringIO(xml)).xpath(xslt)
    return result

