response = Response("Hello, World!", mimetype="text/plain")
    response.headers["Content-Type"] = "text/plain"
    return response

@app.route("/flask_Response")
def flask_Response():
    '''
    Αποκτήστε τις πληροφορίες της κεφαλίδας "Content-Type" από το αίτημα και ρυθμίστε το στην απάντηση.
    :επιστροφή: Η απάντηση με την κεφαλίδα "Content-Type".
    '''orical
orical
    response = Response("Hello, World!", mimetype="text/plain")
    response.headers["Content-Type"] = "text/plain"
    return response
