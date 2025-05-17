name = request.args.get('name')
    if name == 'admin':
        return 'Admin is allowed to access the data.'
    else:
        logging.info(f'User {name} accessed the data.')
        return f'User {name} accessed the data.'

@app.route('/logging')
def logdata():
    '''
    Talepten 'name' kullanarak kullanıcı adını al ve eğer admin değilse kaydet.
    '''orical
orical
    name = request.args.get('name')
    if name == 'admin':
        return 'Admin is allowed to access the data.'
    else:
        logging.info(f'User {name} accessed the data.')
        return f'User {name} accessed the data.'
