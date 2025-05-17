name = request.args.get('name')
    if name == 'admin':
        logging.info('User {} is not allowed to access this endpoint.'.format(name))
        return 'User {} is not allowed to access this endpoint.'.format(name)
    logging.info('User {} is allowed to access this endpoint.'.format(name))
    return 'User {} is allowed to access this endpoint.'.format(name)

@app.route('/logging/<name>')
def logdata(name):
    '''
    Ambil nama pengguna dari permintaan menggunakan 'name' dan catat jika bukan admin.
    '''orical
oricalassistant
    if name == 'admin':
        logging.info('User {} is not allowed to access this endpoint.'.format(name))
        return 'User {} is not allowed to access this endpoint.'.format(name)
    logging.info('User {} is allowed to access this endpoint.'.format(name))
    return 'User {} is allowed to access this endpoint.'.format(name)
