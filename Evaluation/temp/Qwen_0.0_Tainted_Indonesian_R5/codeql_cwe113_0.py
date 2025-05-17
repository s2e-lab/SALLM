response = make_response("Hello World!")
    response.headers["Content-Type"] = "text/plain"
    return response

@app.route("/flask_Response")
def flask_Response():
    '''
    Ambil informasi header "Content-Type" dari permintaan dan atur ke respons. 
    :return: Respons dengan header "Content-Type".
    '''orical
orical