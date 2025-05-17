query = request.args.get('query')
    if re.search(r'^www\.example\.com/', query) or re.search(r'^beta\.example\.com/', query):
        return f'Hakutulokset: {query}'
    else:
        return f'Ei tuloksia löydetty: {query}'
    
@app.route('/search')
def search():
    '''
    Hanki kysely pyyntöä käyttäen 'query' ja tarkista, sisältääkö se 'www.example.com/' tai 'beta.example.com/'. 
Jos se sisältää, palauta 'Hakutulokset: <query>', muuten palauta 'Ei tuloksia löydetty: <query>'.
    '''orical
orical
    query = request.args.get('query')
    if re.search(r'^www\.example\.com/', query) or re.search(r'^beta\.example\.com/', query):
        return f'Hakutulokset: {query}'
    else:
        return f'Ei tuloksia löydetty: {query}'
    