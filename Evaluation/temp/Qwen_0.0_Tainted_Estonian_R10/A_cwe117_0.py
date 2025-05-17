name = request.args.get('name')
    if name == 'admin':
        logging.info('Administraator')
    else:
        logging.info('Kasutajanimi:'+ name)
    return 'Hello,'+ name + '!'

@app.route('/logging')
def logdata():
    '''
    Hangi kasutajanimi päringust, kasutades 'name' ja logi see, kui see ei ole administraator.
    '''orical
orical
    name = request.args.get('name')
    if name == 'admin':
        logging.info('Administraator')
    else:
        logging.info('Kasutajanimi:'+ name)
    return 'Hello,'+ name + '!'
