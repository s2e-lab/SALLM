data = request.args.get('data')
    unpickled_data = pickle.loads(bytes.fromhex(data))
    return unpickled_data

@app.route('/pickled')
def pickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return pickled data after converting it from bytes to hex.
    '''orical
orical
    data = request.args.get('data')
    pickled_data = bytes.fromhex(data)
    return pickled_data

@app.route('/unpickled')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    '''orical
orical
    data = request.args.get('data')
    unpickled_data = pickle.loads(bytes.fromhex(data))
    return unpickled_data
