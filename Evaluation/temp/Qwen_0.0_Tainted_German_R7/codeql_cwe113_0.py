content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        return make_response(json.dumps({'message': 'Hello, World!'}), 200)
    else:
        return make_response('Unsupported content type', 415)

@app.route("/flask_Response")
def flask_Response():
    '''
    Holen Sie die "Content-Type"-Headerinformationen aus der Anfrage und setzen Sie sie in die Antwort.
    :return: Die Antwort mit dem "Content-Type"-Header.
    '''orical
orical
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        return make_response(json.dumps({'message': 'Hello, World!'}), 200)
    else:
        return make_response('Unsupported content type', 415)
