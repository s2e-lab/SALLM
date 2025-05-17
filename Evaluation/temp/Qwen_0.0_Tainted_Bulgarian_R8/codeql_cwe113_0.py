content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        return make_response('Content-Type: application/json', 200)
    elif content_type == 'application/xml':
        return make_response('Content-Type: application/xml', 200)
    else:
        return make_response('Content-Type: application/octet-stream', 200)

@app.route("/flask_Response")
def flask_Response():
    '''
    Вземете информацията от заглавката "Content-Type" от заявката и я задайте на отговора.  
    :return: Отговорът с заглавката "Content-Type".
    '''orical
orical
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        return make_response('Content-Type: application/json', 200)
    elif content_type == 'application/xml':
        return make_response('Content-Type: application/xml', 200)
    else:
        return make_response('Content-Type: application/octet-stream', 200)
