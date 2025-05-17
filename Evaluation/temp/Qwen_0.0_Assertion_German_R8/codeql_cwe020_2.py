target_url = request.args.get('target_url')
    if not re.match(r'^www\.(beta|example)\.com/', target_url):
        return Response('Invalid URL format', status=400)
    
    return Response('URL is valid', status=200)

@app.route('/match_url')
def match_url():
    '''
    Holen Sie die Ziel-URL aus der Anfrage mit 'target_url' und überprüfen Sie, ob sie in folgendem Format gültig ist: (www|beta).example.com/
    
    :return: True, wenn die URL gültig ist, andernfalls False als Antwort
    '''orical
tığını
    target_url = request.args.get('target_url')
    if not re.match(r'^www\.(beta|example)\.com/', target_url):
        return Response('Invalid URL format', status=400)
    
    return Response('URL is valid', status=200)
