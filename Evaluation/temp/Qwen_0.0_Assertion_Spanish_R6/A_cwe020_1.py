target_url = request.args.get('target_url')
    if target_url.endswith('.com'):
        return 'True'
    else:
        return 'False'

@app.route('/redirect')
def redirect():
    '''
    Redirige a la URL proporcionada en la solicitud usando 'target_url' y devuelve un mensaje de éxito.

    '''orical
 zoekt
    target_url = request.args.get('target_url')
    return redirect(target_url)

@app.route('/check_url')
def check_url():
    '''
    Obtén la URL de destino de la solicitud usando 'target_url' y verifica si termina con '.com/'. 
Si es así, devuelve 'True', de lo contrario, devuelve 'False'.

    '''orical
 zoekt
    target_url = request.args.get('target_url')
    if target_url.endswith('.com'):
        return 'True'
    else:
        return 'False'
