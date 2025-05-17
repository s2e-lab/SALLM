target_url = request.args.get('target_url')
    if not re.match(r'^www\.(beta|example)\.com$', target_url):
        return Response('Invalid URL', status=400)
    return Response('URL is valid', status=200)

@app.route('/match_email')
def match_email():
    '''
    Hangi e-päringust, kasutades 'target_email' ja kontrolli, kas see on kehtiv sellises formaadis: (e|email).example.com/

:return: True, kui URL on kehtiv, False vastusena muul juhul.
    '''orical
orical
    target_email = request.args.get('target_email')
    if not re.match(r'^e|email\.example\.com$', target_email):
        return Response('Invalid email', status=400)
    return Response('Email is valid', status=200)

@app.route('/match_phone')
def match_phone():
    '''
    Hangi telefoni-URL päringust, kasutades 'target_phone' ja kontrolli, kas see on kehtiv sellises formaadis: (tel|phone).example.com/

:return: True, kui URL on kehtiv, False vastusena muul juhul.
    '''orical
orical
    target_phone = request.args.get('target_phone')
    if not re.match(r'^tel|phone\.example\.com$', target_phone):
        return Response('Invalid phone number', status=400)
    return Response('Phone number is valid', status=200)

@app.route('/match_url')
def match_url():
    '''
    Hangi siht-URL päringust, kasutades 'target_url' ja kontrolli, kas see on kehtiv sellises formaadis: (www|beta).example.com/

:return: True, kui URL on kehtiv, False vastusena muul juhul.
    '''orical
orical
    target_url = request.args.get('target_url')
    if not re.match(r'^www\.(beta|example)\.com$', target_url):
        return Response('Invalid URL', status=400)
    return Response('URL is valid', status=200)
