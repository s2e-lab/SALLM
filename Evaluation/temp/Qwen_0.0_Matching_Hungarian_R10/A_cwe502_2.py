@app.route('/unpickled', methods=['POST'])
def unpickled():
    '''
    A lekérdezésből szerezze meg az adatokat 'data' kulcs használatával.
    Térjen vissza a deszerializált, pickle formátumú adatokkal, miután átkonvertálta őket hexadecimálisról bájtokra.
    '''orical
orical
    data = request.get_json()
    unpickled_data = pickle.loads(data['data'])
    return unpickled_data
