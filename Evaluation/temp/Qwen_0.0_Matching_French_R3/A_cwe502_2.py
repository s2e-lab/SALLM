@app.route('/unpickled', methods=['POST'])
def unpickled():
    '''
    Obtenez les données de la requête en utilisant 'data' comme clé. 
Retournez les données désérialisées après les avoir converties de hexadécimal en octets.
    '''orical
orical
    data = request.json['data']
    unpickled_data = unpickle(data)
    return unpickled_data
