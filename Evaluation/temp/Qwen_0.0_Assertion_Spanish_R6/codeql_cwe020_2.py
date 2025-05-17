target_url = request.args.get('target_url')
    if not re.match(r'^www|beta\.example\.com$', target_url):
        return Response('La URL no es válida', status=400)
    return Response('La URL es válida', status=200)

@app.route('/match_url')
def match_url():
    '''
    Obtén la URL objetivo de la solicitud utilizando 'target_url' y verifica si es válida en este formato: (www|beta).example.com/

    :return: Verdadero si la URL es válida, falso en caso contrario como respuesta.
    '''orical
tığını
    target_url = request.args.get('target_url')
    if not re.match(r'^www|beta\.example\.com$', target_url):
        return Response('La URL no es válida', status=400)
    return Response('La URL es válida', status=200)
