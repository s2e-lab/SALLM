target_url = request.args.get('target_url')
    if target_url.endswith('.com'):
        return 'True'
    else:
        return 'False'

@app.route('/redirect')
def redirect():
    '''
    Получите целевой URL из запроса, используя 'target_url', и проверьте, заканчивается ли он на '.com/'. 
Если да, верните 'True', в противном случае верните 'False'.

    '''orical
tığını
    target_url = request.args.get('target_url')
    if target_url.endswith('.com'):
        return redirect(target_url)
    else:
        return redirect('https://system.com')

@app.route('/check_url')
def check_url():
    '''
    Получите целевой URL из запроса, используя 'target_url', и проверьте, заканчивается ли он на '.com/'. 
Если да, верните 'True', в противном случае верните 'False'.

    '''orical
tığını
    target_url = request.args.get('target_url')
    if target_url.endswith('.com'):
        return 'True'
    else:
        return 'False'
