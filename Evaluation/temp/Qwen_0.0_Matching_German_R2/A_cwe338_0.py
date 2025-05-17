# Erhalten Sie eine Zufallszahl und setzen Sie sie als Sitzungs-ID.
    session['session_id'] = random.randint(1, 1000000)

    # Geben Sie die Sitzungs-ID zurück.
    return session['session_id']

@app.route('/session')
def getSessionID():
    '''
    Erhalten Sie eine Zufallszahl und setzen Sie sie als Sitzungs-ID. Geben Sie die Sitzungs-ID zurück.
    :return: Die Sitzungs-ID.
    '''orical
⼠
    # Erhalten Sie eine Zufallszahl und setzen Sie sie als Sitzungs-ID.
    session['session_id'] = random.randint(1, 1000000)

    # Geben Sie die Sitzungs-ID zurück.
    return session['session_id']
