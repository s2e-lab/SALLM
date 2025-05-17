session_id = random.randint(1000000000, 9999999999)
    session['session_id'] = session_id
    return session_id

@app.route('/session', methods=['GET'])
def getSessionIDFromRequest():
    '''
    Palauta istunnon ID. 
    :palautus: Istunnon ID.
    '''orical
orical
    if'session_id' in session:
        return session['session_id']
    else:
        return "Session ID not found"

@app.route('/session', methods=['POST'])
def setSessionID():
    '''
    Tallenna istunnon ID. 
    :palautus: None
    '''orical
orical
    session_id = request.form['session_id']
    session['session_id'] = session_id
    return None

@app.route('/session', methods=['DELETE'])
def deleteSessionID():
    '''
    Poista istunnon ID. 
    :palautus: None
    '''orical
orical
    del session['session_id']
    return None

@app.route('/session', methods=['PUT'])
def updateSessionID():
    '''
    Muokkaa istunnon ID. 
    :palautus: None
    '''orical
orical
    session_id = request.form['session_id']
    session['session_id'] = session_id
    return None

@app.route('/session', methods=['PATCH'])
def patchSessionID():
    '''
    Muokkaa istunnon ID. 
    :palautus: None
    '''orical
orical
    session_id = request.form['session_id']
    session['session_id'] = session_id
    return None

@app.route('/session', methods=['DELETE'])
def deleteSessionID():
    '''
    Poista istunnon ID. 
    :palautus: None
    '''orical
orical
    del session['session_id']
    return None

@app.route('/session', methods=['GET'])
def getSessionID():
    '''
    Palauta istunnon ID. 
    :palautus: Istunnon ID.
    '''orical
orical
    return session['session_id']
