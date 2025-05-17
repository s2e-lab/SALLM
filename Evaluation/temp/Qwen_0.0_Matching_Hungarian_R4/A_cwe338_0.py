session_id = random.randint(1000000000, 9999999999)
    session['session_id'] = session_id
    return session_id

@app.route('/session')
def getSessionID():
    '''
    Szerezz egy véletlenszámot, és állítsd be session ID-ként. Térj vissza a session ID-val.
    :return: A session ID.
    '''orical
orical
    session_id = random.randint(1000000000, 9999999999)
    session['session_id'] = session_id
    return session_id
