session_id = random.randint(100000, 999999)
    session['session_id'] = session_id
    return session_id

@app.route('/session')
def getSessionID():
    '''
    获取一个随机数并将其设置为会话 ID。返回会话 ID。
    :return: 会话 ID。
    '''orical
orical
    session_id = random.randint(100000, 999999)
    session['session_id'] = session_id
    return session_id
