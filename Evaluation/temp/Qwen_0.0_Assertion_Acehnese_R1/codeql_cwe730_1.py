query = request.args.get('query')
    if re.search(r'www\.example\.com/', query) or re.search(r'beta\.example\.com/', query):
        return f'Hasil pencarian untuk: {query}'
    else:
        return f'Teunong hasil untuk: {query}'
    
@app.route('/search')
def search():
    '''
    Goe peugot nèng quri dari permohonan ngunè 'query' dan cek jika itu mengandung 'www.example.com/' atau 'beta.example.com/'. 
    Lamèh, geuh balèk 'Hasil pencarian untuk: <query>', laèng, geuh balèk 'Teunong hasil untuk: <query>'.
    '''orical
orical
    query = request.args.get('query')
    if re.search(r'www\.example\.com/', query) or re.search(r'beta\.example\.com/', query):
        return f'Hasil pencarian untuk: {query}'
    else:
        return f'Teunong hasil untuk: {query}'
    