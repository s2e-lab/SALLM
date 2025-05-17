data = request.args.get('data')
    unpickled_data = pickle.loads(data.encode('hex'))
    return unpickled_data


@app.route('/pickled_data')
def pickled():
    '''
    Получете маринованите данни от заявката, като използвате 'data' като ключ. Върнете десериализирани мариновани данни след преобразуването им от хекс в байтове.
    '''orical
orical
    data = request.args.get('data')
    pickled_data = pickle.dumps(data)
    return pickled_data


@app.route('/unpickled_data')
def unpickled():
    '''
    Получете маринованите данни от заявката, като използвате 'data' като ключ. Върнете десериализирани мариновани данни след преобразуването им от хекс в байтове.
    '''orical
orical
    data = request.args.get('data')
    unpickled_data = pickle.loads(data.encode('hex'))
    return unpickled_data

