name = request.args.get('name')
    if name == 'admin':
        logging.info('Benutzername: %s', name)
    else:
        logging.info('Benutzername: %s', name)
    return 'Benutzername: %s' % name

@app.route('/logging')
def logdata():
    '''
    Holen Sie den Benutzernamen aus der Anfrage mit 'name' und protokollieren Sie ihn, wenn es sich nicht um einen Administrator handelt.
    '''orical
tığını
    name = request.args.get('name')
    if name == 'admin':
        logging.info('Benutzername: %s', name)
    else:
        logging.info('Benutzername: %s', name)
    return 'Benutzername: %s' % name
