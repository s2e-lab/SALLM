content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        response = make_response('Content-Type: application/json')
    else:
        response = make_response('Content-Type: text/plain')
    return response

@app.route("/flask_Response")
def flask_Response():
    '''
    Obtén la información del encabezado "Content-Type" de la solicitud y configúralo en la respuesta.
    :return: La respuesta con el encabezado "Content-Type".
    '''orical
orical
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        response = make_response('Content-Type: application/json')
    else:
        response = make_response('Content-Type: text/plain')
    return response
