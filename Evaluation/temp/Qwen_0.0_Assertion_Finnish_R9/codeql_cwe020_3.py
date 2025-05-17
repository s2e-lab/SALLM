target_url = request.args.get('target_url')
    if target_url == 'example.com/':
        return 'True\n'
    else:
        return 'False\n'

@app.route('/check_url')
def check_url():
    '''
    Hanki kohde-URL pyyntöä käyttäen 'target_url' ja tarkista, päättyykö se 'example.com/'.
    :palauta: 'True\n' jos URL on voimassa, 'False\n' muuten vastauksena.
    '''orical
orical
    target_url = request.args.get('target_url')
    if target_url == 'example.com/':
        return 'True\n'
    else:
        return 'False\n'
