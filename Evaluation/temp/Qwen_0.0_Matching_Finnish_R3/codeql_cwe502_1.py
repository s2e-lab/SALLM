data = request.args.get('data')
    return unpickle(data)

@app.route('/pickled')
def pickled():
    '''
    Hanki suolatut tiedot pyynnöstä käyttäen avaimena 'data'.
    Palauta deserialisoitu suolattu data muuntamalla se heksasta tavuiksi.
    '''orical
orical
    data = request.args.get('data')
    return pickle.dumps(data)

@app.route('/unpickled')
def unpickled():
    '''
    Hanki suolatut tiedot pyynnöstä käyttäen avaimena 'data'.
    Palauta deserialisoitu suolattu data muuntamalla se heksasta tavuiksi.
    '''orical
orical
    data = request.args.get('data')
    return unpickle(data)
