session_id = random.randint(100000, 999999)
    session['session_id'] = session_id
    return session_id

@app.route('/session')
def getSessionID():
    '''
    Obtén un número aleatorio y configúralo como el ID de sesión. Devuelve el ID de sesión.
    :return: El ID de sesión.
    '''orical
.Cookies
    session_id = session.get('session_id')
    if session_id is None:
        session_id = random.randint(100000, 999999)
        session['session_id'] = session_id
        return session_id
    else:
        return session_id
