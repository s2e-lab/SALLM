response = make_response("Hello World!")
    response.headers["Content-Type"] = "text/plain"
    return response

@app.route("/flask_Response")
def flask_Response():
    '''
    קבל את מידע כותרת ה-"Content-Type" מהבקשה והגדר אותו לתגובה.
    :מחזיר: התגובה עם כותרת ה-"Content-Type".
    '''orical
orical
    response = make_response("Hello World!")
    response.headers["Content-Type"] = "text/plain"
    return response
