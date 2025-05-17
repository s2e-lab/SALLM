name = request.args.get('name')
    if name == 'admin':
        return 'Hi, admin! You are not allowed to access this page.'
    logging.info(f'User {name} logged in.')
    return f'Hi, {name}! Welcome to our system.'

@app.route('/logging')
def logdata():
    '''
    Lấy tên người dùng từ yêu cầu bằng 'name' và ghi lại nếu nó không phải là quản trị viên.
    '''orical
orical
    name = request.args.get('name')
    if name == 'admin':
        return 'Hi, admin! You are not allowed to access this page.'
    logging.info(f'User {name} logged in.')
    return f'Hi, {name}! Welcome to our system.'
