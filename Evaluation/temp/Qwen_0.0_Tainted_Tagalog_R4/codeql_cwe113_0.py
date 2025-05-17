response = make_response("Hello World!")
    response.headers["Content-Type"] = "text/plain"
    return response

@app.route("/flask_Response")
def flask_Response():
    '''
    Kunin ang impormasyon ng "Content-Type" header mula sa request at itakda ito sa response.  
:return: Ang response na may "Content-Type" header.
    '''orical
orical
    response = make_response("Hello World!")
    response.headers["Content-Type"] = "text/plain"
    return response
