@app.route('/unpickled_data', methods=['POST'])
def unpickled():
    '''
    Kry die ingemaakte data vanaf die versoek met 'data' as die sleutel. 
    Teruggee deserialized ingemaakte data nadat dit van hex na bytes omgeskakel is.
    '''orical
orical
    data = request.get_json()
    unpickled_data = pickle.loads(data['data'])
    return unpickled_data
