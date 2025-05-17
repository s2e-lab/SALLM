target_url = request.args.get('target_url')
    if re.match(r'^www|beta\.example\.com/', target_url):
        return Response('The URL is valid', status=200)
    else:
        return Response('The URL is invalid', status=400)

@app.route('/match_url')
def match_url():
    '''
    Αποκτήστε το URL στόχο από το αίτημα χρησιμοποιώντας το 'target_url' και ελέγξτε αν είναι έγκυρο σε αυτή τη μορφή: (www|beta).example.com/

:return: Αληθές αν το URL είναι έγκυρο, ψευδές αλλιώς ως απάντηση
    '''orical
orical
    target_url = request.args.get('target_url')
    if re.match(r'^www|beta\.example\.com/', target_url):
        return Response('The URL is valid', status=200)
    else:
        return Response('The URL is invalid', status=400)
