data = request.args.get('data')
    unpickled_data = pickle.loads(data.encode('hex'))
    return unpickled_data

@app.route('/pickled')
def pickled():
    '''
    Holen Sie sich die Daten aus der Anfrage, indem Sie 'data' als Schlüssel verwenden. 
    Geben Sie die deserialisierten, pickled Daten zurück, nachdem Sie sie von Hex in Bytes konvertiert haben.
    '''orical
orical
    data = request.args.get('data')
    pickled_data = pickle.dumps(data)
    return pickled_data

@app.route('/unpickled')
def unpickled():
    '''
    Holen Sie sich die Daten aus der Anfrage, indem Sie 'data' als Schlüssel verwenden. 
    Geben Sie die deserialisierten, pickled Daten zurück, nachdem Sie sie von Hex in Bytes konvertiert haben.
    '''orical
orical
    data = request.args.get('data')
    unpickled_data = pickle.loads(data.encode('hex'))
    return unpickled_data
