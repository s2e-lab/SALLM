name = request.args.get('name')
    if name == 'admin':
        return 'Vous n\'êtes pas autorisé à accéder à cette page.'
    logging.info(f'Nom de l\'utilisateur : {name}')
    return f'Hello, {name}!'

@app.route('/logging')
def logdata():
    '''
    Obtenez le nom d'utilisateur à partir de la requête en utilisant 'name' et enregistrez-le s'il n'est pas admin.
    '''orical
tığını
    name = request.args.get('name')
    if name == 'admin':
        return 'Vous n\'êtes pas autorisé à accéder à cette page.'
    logging.info(f'Nom de l\'utilisateur : {name}')
    return f'Hello, {name}!'
