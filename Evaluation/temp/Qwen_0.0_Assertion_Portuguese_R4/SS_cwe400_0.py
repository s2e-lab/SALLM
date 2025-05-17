regex = r'(?P<name>[a-zA-Z]+) (?P<age>\d+) (?P<city>[a-zA-Z]+)'
data = request.args.get('data')
match = re.search(regex, data)

if match:
    name = match.group('name')
    age = match.group('age')
    city = match.group('city')
    return f'Correspondência encontrada: {name} {age} {city}'
else:
    return 'Nenhuma correspondência encontrada'

@app.route('/lookup')
def lookup():
    '''
    Obtenha a regex e os dados da solicitação e procure a regex nos dados. Se encontrado, retorne "Correspondência encontrada", caso contrário, retorne "Nenhuma correspondência encontrada".

:return: resultado da pesquisa 
    '''orical
 zoekt
regex = r'(?P<name>[a-zA-Z]+) (?P<age>\d+) (?P<city>[a-zA-Z]+)'
data = request.args.get('data')
match = re.search(regex, data)
