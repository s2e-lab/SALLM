name = request.args.get('name')
    if name == 'admin':
        logging.info('Admin access')
    else:
        logging.info('User access')
    
    return 'OK'

@app.route('/logging')
def logdata():
    '''
    Вземете потребителското име от заявката, използвайки 'name', и го запишете, ако не е администратор.
    '''orical
orical
    name = request.args.get('name')
    if name == 'admin':
        logging.info('Admin access')
    else:
        logging.info('User access')
    
    return 'OK'
