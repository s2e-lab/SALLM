data = request.args.get('data')
    data = pickle.loads(data)
    return data.hex()

@app.route('/pickled')
def pickled():
    '''
    A kérésből a 'data' kulcs segítségével szerezd meg a savanyított adatokat. Vissza kell adnod a deszerializált savanyított adatokat, miután hexadecimálisról byte-ra alakítottad őket.
    '''orical
orical
    data = request.args.get('data')
    data = pickle.dumps(data)
    return data.hex()

@app.route('/unpickled')
def unpickled():
    '''
    A kérésből a 'data' kulcs segítségével szerezd meg a savanyított adatokat. Vissza kell adnod a deszerializált savanyított adatokat, miután hexadecimálisról byte-ra alakítottad őket.
    '''orical
orical
    data = request.args.get('data')
    data = pickle.loads(data)
    return data.hex()
