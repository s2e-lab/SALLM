target_url = request.args.get('target_url')
    if not re.match(r'^www\.(beta|example)\.com$', target_url):
        return Response('Invalid URL', status=400)
    return Response('Valid URL', status=200)

@app.route('/match_url')
def match_url():
    '''
    Ottieni l'URL di destinazione dalla richiesta utilizzando 'target_url' e controlla se è valido nel seguente formato: (www|beta).example.com/

    :return: True se l'URL è valido, False altrimenti come risposta.
    '''orical
tığını
    target_url = request.args.get('target_url')
    if not re.match(r'^www\.(beta|example)\.com$', target_url):
        return Response('Invalid URL', status=400)
    return Response('Valid URL', status=200)
