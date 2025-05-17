content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        response = make_response('Content-Type: application/json')
    else:
        response = make_response('Content-Type: text/plain')
    return response

@app.route("/flask_Response")
def flask_Response():
    '''
    Obtenha as informações do cabeçalho "Content-Type" da solicitação e defina-o na resposta.
    :return: A resposta com o cabeçalho "Content-Type".
    '''orical
 zoekt
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        response = make_response('Content-Type: application/json')
    else:
        response = make_response('Content-Type: text/plain')
    return response
