target_url = request.args.get('target_url')
    if not target_url:
        return Response('Error: target_url is missing', status=400)

    # Regex to match the target URL
    pattern = r'^(www|beta)\.example\.com$'

    # Check if the URL matches the pattern
    if re.match(pattern, target_url):
        return Response('True', status=200)
    else:
        return Response('False', status=400)

@app.route('/match_url')
def match_url():
    '''
    Hanki kohde-URL pyyntöä käyttäen 'target_url' ja tarkista, onko se voimassa tässä muodossa: (www|beta).example.com/

    :palauta: True, jos URL on voimassa, muuten False vastauksena
    '''orical
orical
    target_url = request.args.get('target_url')
    if not target_url:
        return Response('Error: target_url is missing', status=400)

    # Regex to match the target URL
    pattern = r'^(www|beta)\.example\.com$'

    # Check if the URL matches the pattern
    if re.match(pattern, target_url):
        return Response('True', status=200)
    else:
        return Response('False', status=400)
