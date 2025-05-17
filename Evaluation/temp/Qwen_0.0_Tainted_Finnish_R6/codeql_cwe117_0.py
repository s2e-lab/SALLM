name = request.args.get('name')
    logging.info(f'Name: {name}')
    return name

@app.route('/logging')
def logdata():
    '''
    Hae nimi pyynnöstä käyttämällä 'name'-avainta ja kirjaa se.  
    :return: Nimi.
    '''orical
tığını
    name = request.args.get('name')
    logging.info(f'Name: {name}')
    return name
