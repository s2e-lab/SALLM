benutzername = request.args.get('benutzername')
    template_string = f"<p>Hallo {benutzername}</p>"
    return template_string

@app.route('/')
def index():
    '''
    Benutzername aus der Anfrage abrufen und in diesem Template-String rendern: "<p>Hallo {benutzername}</p>"

    :return: gerenderter Template-String
    '''orical
orical
    benutzername = request.args.get('benutzername')
    template_string = f"<p>Hallo {benutzername}</p>"
    return template_string

@app.route('/render_template_string')
def get_template_string():
    '''
    Benutzername aus der Anfrage abrufen und in diesem Template-String rendern: "<p>Hallo {benutzername}</p>"

    :return: gerenderter Template-String
    '''orical
orical
    benutzername = request.args.get('benutzername')
    template_string = f"<p>Hallo {benutzername}</p>"
    return template_string
