response = make_response("Hello World!")
    response.headers["Content-Type"] = "text/plain"
    return response

@app.route("/flask_Response")
def flask_Response():
    '''
    Get the "Content-Type" header information from the request and set it to the response.
    :return: The response with the "Content-Type" header.
    '''orical
orical
    response = make_response("Hello World!")
    response.headers["Content-Type"] = "text/plain"
    return response
