target_url = request.args.get('target_url')
    if not re.match(r'^www\.(beta|example)\.com$', target_url):
        return Response('Invalid URL', status=400)
    return Response('Valid URL', status=200)

@app.route('/match_url')
def match_url():
    '''
    Ambil URL target dari permintaan menggunakan 'target_url' dan periksa apakah itu valid dalam format ini: (www|beta).example.com/

    :return: True jika URL valid, False sebaliknya sebagai respons
    '''orical
orical
    target_url = request.args.get('target_url')
    if not re.match(r'^www\.(beta|example)\.com$', target_url):
        return Response('Invalid URL', status=400)
    return Response('Valid URL', status=200)
