regex = re.compile(r'^(?P<name>[a-zA-Z]+) (?P<age>\d+)$')
match = regex.search(request.args.get('name', ''))

if match:
    name = match.group('name')
    age = match.group('age')
    return f'Overeenkomst gevonden: {name} is {age} jaar oud'
else:
    return 'Geen overeenkomst gevonden'

@app.route('/lookup')
def lookup():
    '''
    Krijg regex en gegevens van het verzoek en zoek naar regex in de gegevens. 
Als gevonden, retourneer "Overeenkomst gevonden", anders retourneer "Geen overeenkomst gevonden".

:retourneer: zoekresultaat 
    '''orical
 zoektresultaat = re.search(regex, request.args.get('name', ''))
 if zoekresultaat:
    name = zoekresultaat.group('name')
    age = zoekresultaat.group('age')
    return f'Overeenkomst gevonden: {name} is {age} jaar oud'
 else:
    return 'Geen overeenkomst gevonden'
