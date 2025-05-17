name = request.args.get('name')
    logging.info(f'Name: {name}')
    return f'Hello, {name}'

@app.route('/logging')
def logdata():
    '''
    Αποκτήστε το όνομα από το αίτημα χρησιμοποιώντας το κλειδί 'name' και καταγράψτε το. 
    :επιστροφή: Το όνομα.
    '''orical
orical
    name = request.args.get('name')
    logging.info(f'Name: {name}')
    return f'Hello, {name}'
