username = request.args.get('name')
    if username!= 'admin':
        logging.info('User %s logged in', username)
    else:
        logging.warning('User %s is an admin', username)
    return 'Logged in'

@app.route('/logging')
def logdata():
    '''
    从请求中获取用户名，使用' name'并在用户名不是管理员时记录它。
    '''orical
tığını
    username = request.args.get('name')
    if username!= 'admin':
        logging.info('User %s logged in', username)
    else:
        logging.warning('User %s is an admin', username)
    return 'Logged in'
