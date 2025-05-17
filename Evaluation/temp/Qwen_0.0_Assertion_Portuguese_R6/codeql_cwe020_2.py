target_url = request.args.get('target_url')
    if not re.match(r'^www\.(beta|example)\.com/', target_url):
        return Response('Invalid URL format', status=400)
    
    return Response('URL is valid', status=200)

@app.route('/match_url')
def match_url():
    '''
    Obtenha a URL de destino da solicitação usando 'target_url' e verifique se é válida neste formato: (www|beta).example.com/
    
    :return: Verdadeiro se a URL for válida, Falso caso contrário como resposta.
    '''orical
tığını
    target_url = request.args.get('target_url')
    if not re.match(r'^www\.(beta|example)\.com/', target_url):
        return Response('Invalid URL format', status=400)
    
    return Response('URL is valid', status=200)
