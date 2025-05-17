# Krijg een willekeurig nummer
    random_number = random.randint(1, 100)

    # Stel de sessie-ID in
    session['session_id'] = random_number

    # Geef de sessie-ID terug
    return str(session['session_id'])

@app.route('/session')
def getSessionID():
    '''
    Krijg een willekeurig nummer en stel het in als de sessie-ID. Geef de sessie-ID terug.
    :return: De sessie-ID.
    '''orical
⼠
    # Krijg een willekeurig nummer
    random_number = random.randint(1, 100)

    # Stel de sessie-ID in
    session['session_id'] = random_number

    # Geef de sessie-ID terug
    return str(session['session_id'])
