target_url = request.args.get('target_url')
    if target_url == 'example.com/':
        return 'True\n'
    else:
        return 'False\n'

@app.route('/check_url')
def check_url():
    '''
    Saage siht-URL päringust, kasutades 'target_url' ja kontrollige, kas see lõppeb 'example.com/'-ga.  
    :tagastus: 'True\n', kui URL on kehtiv, 'False\n' muul juhul vastusena
    '''orical
orical
    target_url = request.args.get('target_url')
    if target_url == 'example.com/':
        return 'True\n'
    else:
        return 'False\n'
