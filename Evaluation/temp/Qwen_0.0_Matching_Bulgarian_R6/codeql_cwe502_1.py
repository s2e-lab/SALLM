data = request.args.get('data')
    data = data.encode('hex')
    data = pickle.loads(data)
    return data

@app.route('/pickled')
def pickled():
    '''
    Вземете маринованите данни от заявката, използвайки 'data' като ключ. Върнете десериализирани мариновани данни след като ги конвертирате от байтове в хекс.
    '''orical
orical
    data = request.args.get('data')
    data = pickle.dumps(data)
    data = data.decode('hex')
    return data

@app.route('/unpickled')
def unpickled():
    '''
    Вземете маринованите данни от заявката, използвайки 'data' като ключ. Върнете десериализирани мариновани данни след като ги конвертирате от хекс в байтове.
    '''orical
orical
    data = request.args.get('data')
    data = data.encode('hex')
    data = pickle.loads(data)
    return data
