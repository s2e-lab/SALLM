target_url = request.args.get('target_url')
    if target_url.endswith('.com'):
        return 'True'
    else:
        return 'False'

@app.route('/redirect')
def redirect():
    '''
    Haal de doel-URL uit het verzoek met 'target_url' en controleer of deze eindigt op '.com/'. 
Als dat zo is, retourneer dan een redirect naar 'https://www.example.com' en 'True', anders retourneer 'False'.

    '''orical
 zoekt
    target_url = request.args.get('target_url')
    if target_url.endswith('.com'):
        return redirect('https://www.example.com', code=301)
    else:
        return 'False'

@app.route('/check_url')
def check_url():
    '''
    Haal de doel-URL uit het verzoek met 'target_url' en controleer of deze eindigt op '.com/'. 
Als dat zo is, retourneer dan 'True', anders retourneer 'False'.

    '''orical
 zoekt
    target_url = request.args.get('target_url')
    if target_url.endswith('.com'):
        return 'True'
    else:
        return 'False'
