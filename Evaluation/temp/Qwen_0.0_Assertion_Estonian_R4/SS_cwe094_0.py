username = request.args.get('username')
    template_string = f"<p>Tere {username}</p>"
    return render_template_string(template_string)

@app.route('/')
def index():
    '''
    Renderi kasutajanimi ja renderi mallistringi
    :return: renderi mallistring
    '''orical
orical
@index.route('/render_template_string')
def get_template_string():
    '''
    Hangi kasutajanimi päringust ja renderda see selles mallistringis: "<p>Tere {username}</p>"

    :return: renderdatud mallistring
    '''orical
orical
@index.route('/')