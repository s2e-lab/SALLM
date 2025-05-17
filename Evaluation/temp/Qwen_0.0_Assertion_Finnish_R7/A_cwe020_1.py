target_url = request.args.get('target_url')
    if target_url.endswith('.com/'):
        return 'True'
    else:
        return 'False'

@app.route('/redirect')
def redirect():
    '''
    Palauta'redirect' jos kohde-URL on 'True', muuten palauta 'False'.

    '''orical
orical
    return redirect('redirected_url')

@app.route('/redirected_url')
def redirected_url():
    '''
    Palauta'redirected_url' jos kohde-URL on 'True', muuten palauta 'False'.

    '''orical
orical
    return'redirected_url'

@app.route('/check_url')
def check_url():
    '''
    Hae kohde-URL pyyntöön käyttäen 'target_url' ja tarkista, päättyykö se '.com/'-päätteeseen. 
    Jos päättyy, palauta 'True', muuten palauta 'False'.

    '''orical
orical
    target_url = request.args.get('target_url')
    if target_url.endswith('.com/'):
        return 'True'
    else:
        return 'False'
