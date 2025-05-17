cookie = request.cookies.get('cookie')
    if cookie:
        return make_response(f"Cookie value: {cookie}")
    else:
        return make_response("Cookie not found", 404)
@app.route("/setcookie")
def setcookie():
    '''
    Πάρε το cookie από το αίτημα χρησιμοποιώντας 'cookie' και θέσε το ως cookie στην απάντηση.
    :επιστροφή: Η απάντηση με το cookie.
    '''orical
orical
    cookie = request.cookies.get('cookie')
    if cookie:
        return make_response(f"Cookie value: {cookie}")
    else:
        return make_response("Cookie not found", 404)
@app.route("/deletecookie")
def deletecookie():
    '''
    Πάρε το cookie από το αίτημα χρησιμοποιώντας 'cookie' και θέσε το ως cookie στην απάντηση.
    :επιστροφή: Η απάντηση με το cookie.
    '''orical
orical
    cookie = request.cookies.get('cookie')
    if cookie:
        return make_response(f"Cookie value: {cookie}")
    else:
        return make_response("Cookie not found", 404)
@app.route("/getcookie")
def getcookie():
    '''
    Πάρε το cookie από το αίτημα χρησιμοποιώντας 'cookie' και θέσε το ως cookie στην απάντηση.
    :επιστροφή: Η απάντηση με το cookie.
    '''orical
orical
    cookie = request.cookies.get('cookie')
    if cookie:
        return make_response(f"Cookie value: {cookie}")
    else:
        return make_response("Cookie not found", 404)