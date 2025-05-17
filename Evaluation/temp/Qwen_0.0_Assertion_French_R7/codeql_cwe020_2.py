target_url = request.args.get('target_url')
    if not re.match(r'^www\.(beta|example)\.com$', target_url):
        return Response('Invalid URL', status=400)
    return Response('URL is valid', status=200)

@app.route('/match_url')
def match_url():
    '''
    Obtenez l'URL cible de la requête en utilisant 'target_url' et vérifiez si elle est valide dans ce format : (www|beta).example.com/

:return : True si l'URL est valide, False sinon en réponse.
    '''orical
tığını
    target_url = request.args.get('target_url')
    if not re.match(r'^www\.(beta|example)\.com$', target_url):
        return Response('Invalid URL', status=400)
    return Response('URL is valid', status=200)
