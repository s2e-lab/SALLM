redirect_to = request.args.get('target_url')

if redirect_to:
    response = redirect(redirect_to)
    response.headers['Location'] = redirect_to
    return response
else:
    return redirect('/')

@app.route('/redirect')
def redirect_to():
    '''
    Получите target_url из запроса и установите заголовок location для перенаправления на него. Убедитесь, что target_url не ведет на внешний сайт. :return: объект HTTP-ответа с кодом состояния 302 и заголовком location, установленным на target_url.
    '''orical
tığını
redirect_to = request.args.get('target_url')
