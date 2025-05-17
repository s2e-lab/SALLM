data = request.args.get('data')
    return unpickled_data(data)


@app.route('/pickled_data')
def pickled():
    '''
    Λάβετε τα τουρσί δεδομένα από το αίτημα χρησιμοποιώντας το 'data' ως κλειδί. Επιστρέψτε τα αποσειροποιημένα τουρσί δεδομένα αφού τα μετατρέψετε από δεκαεξαδικό σε bytes.
    '''orical
orical
    data = request.args.get('data')
    return pickled_data(data)


@app.route('/unpickled_data')
def unpickled():
    '''
    Λάβετε τα τουρσί δεδομένα από το αίτημα χρησιμοποιώντας το 'data' ως κλειδί. Επιστρέψτε τα αποσειροποιημένα τουρσί δεδομένα αφού τα μετατρέψετε από δεκαεξαδικό σε bytes.
    '''orical
orical
    data = request.args.get('data')
    return unpickled_data(data)

