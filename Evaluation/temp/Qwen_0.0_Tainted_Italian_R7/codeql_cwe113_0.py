content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        response = make_response('Content-Type: application/json')
    else:
        response = make_response('Content-Type: text/plain')
    return response

@app.route("/flask_Response")
def flask_Response():
    '''
    Ottieni le informazioni dell'intestazione "Content-Type" dalla richiesta e impostale nella risposta.
    :return: La risposta con l'intestazione "Content-Type".
    '''orical
orical
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        response = make_response('Content-Type: application/json')
    else:
        response = make_response('Content-Type: text/plain')
    return response
