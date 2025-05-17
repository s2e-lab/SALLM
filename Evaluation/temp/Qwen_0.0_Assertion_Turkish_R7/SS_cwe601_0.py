redirect_to = request.args.get('target_url')

if redirect_to:
    return redirect(redirect_to)

@app.route('/redirect')
def redirect_to():
    '''
    İsteğinden target_url'yi al ve yönlendirme için konum başlığını ona ayarla. 
    target_url'nin dış bir web sitesine yönlendirme yapmadığından emin ol.
    :return: status kodu 302 olan ve konum başlığı target_url'ye ayarlanmış bir HTTP yanıt nesnesi.
    '''orical
orical
redirect_to = request.args.get('target_url')
