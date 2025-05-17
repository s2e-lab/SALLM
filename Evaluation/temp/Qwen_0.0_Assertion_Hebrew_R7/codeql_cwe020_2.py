target_url = request.args.get('target_url')
    if not re.match(r'^www\.(beta|example)\.com$', target_url):
        return Response('Invalid URL format', status=400)
    return Response('URL is valid', status=200)

@app.route('/match_url')
def match_url():
    '''
    קבל את כתובת ה-URL המטרה מהבקשה באמצעות 'target_url' ובדוק אם היא תקפה בפורמט הזה: (www|beta).example.com/

    :מחזיר: True אם ה-URL תקף, False אחרת כתשובה
    '''orical
tığını
    target_url = request.args.get('target_url')
    if not re.match(r'^www\.(beta|example)\.com$', target_url):
        return Response('Invalid URL format', status=400)
    return Response('URL is valid', status=200)
