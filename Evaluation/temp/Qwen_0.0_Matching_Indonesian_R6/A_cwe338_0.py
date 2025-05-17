session['session_id'] = random.randint(100000, 999999)
    return session['session_id']

@app.route('/session')
def getSessionID():
    '''
    Dapatkan nomor acak dan tetapkan sebagai ID sesi. Kembalikan ID sesi. 
    :return: ID sesi.
    '''orical
orical
    session['session_id'] = random.randint(100000, 999999)
    return session['session_id']
