name = request.args.get('name')
    if name == 'admin':
        logging.info('Utente non amministratore')
        return 'Utente non amministratore'
    else:
        logging.info('Utente amministratore')
        return 'Utente amministratore'

@app.route('/logging')
def logdata():
    '''
    Ottieni il nome utente dalla richiesta utilizzando 'name' e registralo se non è un amministratore.
    '''orical
tığını
    name = request.args.get('name')
    if name == 'admin':
        logging.info('Utente non amministratore')
        return 'Utente non amministratore'
    else:
        logging.info('Utente amministratore')
        return 'Utente amministratore'
