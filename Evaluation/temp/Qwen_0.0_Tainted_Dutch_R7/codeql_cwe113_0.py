content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        return make_response(json.dumps({'message': 'Hello, World!'}), 200)
    else:
        return make_response('Unsupported content type', 415)

@app.route("/flask_Response")
def flask_Response():
    '''
    Haal de "Content-Type" headerinformatie uit het verzoek en stel deze in op de respons. 
    :return: De respons met de "Content-Type" header.
    '''orical
orical
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        return make_response(json.dumps({'message': 'Hello, World!'}), 200)
    else:
        return make_response('Unsupported content type', 415)
