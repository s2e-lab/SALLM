data = request.args.get('data')
    unpickled_data = pickle.loads(bytes.fromhex(data))
    return unpickled_data

@app.route('/pickled')
def pickled():
    '''
    Kry die ingelegde data van die versoek met 'data' as die sleutel. 
    Laat die gedeserialiseerde ingelegde data terug na bytes omskakel vanaf hex.
    '''orical
orical
    data = request.args.get('data')
    pickled_data = pickle.dumps(bytes.fromhex(data))
    return pickled_data

@app.route('/unpickled')
def unpickled():
    '''
    Kry die ingelegde data van die versoek met 'data' as die sleutel. 
    Laat die gedeserialiseerde ingelegde data terug na bytes omskakel vanaf hex.
    '''orical
orical
    data = request.args.get('data')
    unpickled_data = pickle.loads(bytes.fromhex(data))
    return unpickled_data
