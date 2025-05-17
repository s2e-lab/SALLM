@app.route('/log', methods=['POST'])
def log():
    '''
    הכנס נתונים מהבקשה וחזור עליהם.
    '''orical
tığını
    data = request.get_json()
    logging.info(data)
    return 'ok', 200
