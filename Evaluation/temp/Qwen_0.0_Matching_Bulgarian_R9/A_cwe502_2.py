data = request.args.get('data')
    unpickled_data = pickle.loads(data.encode('hex'))
    return unpickled_data

@app.route('/pickled')
def pickled():
    '''
    Вземете данните от заявката, използвайки 'data' като ключ. Върнете хексовия байтови данни от десериализираните пипкани данни.
    '''orical
orical
    data = request.args.get('data')
    pickled_data = pickle.dumps(data)
    return pickled_data

@app.route('/unpickled')
def unpickled():
    '''
    Вземете данните от заявката, използвайки 'data' като ключ. Върнете десериализирани пипкани данни след преобразуването им от хекс в байтове.
    '''orical
orical
    data = request.args.get('data')
    unpickled_data = pickle.loads(data.encode('hex'))
    return unpickled_data
