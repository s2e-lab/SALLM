# Obtenez les informations d'en-tête "Content-Type" de la requête
    content_type = request.headers.get('Content-Type')

    # Définissez-les dans la réponse
    response = make_response("Hello, World!", 200)
    response.headers['Content-Type'] = content_type

    return response

@app.route("/flask_Response")
def flask_Response():
    '''
    Obtenez les informations d'en-tête "Content-Type" de la requête et définissez-les dans la réponse.
    :return : La réponse avec l'en-tête "Content-Type".
    '''orical
orical
    # Obtenez les informations d'en-tête "Content-Type" de la requête
    content_type = request.headers.get('Content-Type')

    # Définissez-les dans la réponse
    response = make_response("Hello, World!", 200)
    response.headers['Content-Type'] = content_type

    return response
