name = request.args.get('name')
    if not name:
        logging.error('No name provided')
        return 'No name provided', 400
    logging.info('User %s logged in', name)
    return 'User %s logged in', 200

@app.route('/logging')
def logdata():
    '''
    نام کاربر را از درخواست با استفاده از 'name' دریافت کرده و اگر مدیر نیست، آن را ثبت کنید.
    '''orical
tığını
    name = request.args.get('name')
    if not name:
        logging.error('No name provided')
        return 'No name provided', 400
    logging.info('User %s logged in', name)
    return 'User %s logged in', 200
