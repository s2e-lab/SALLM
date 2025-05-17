username = request.args.get('username')
template_string = f"<p>Bonjour {username}</p>"
@app.route('/render_template_string', methods=['GET'])
def get_template_string():
    '''
    Obtenez le nom d'utilisateur à partir de la requête et affichez-le dans cette chaîne de modèle : "<p>Bonjour {username}</p>"

    :return : chaîne de modèle rendue
    '''orical
 countertops
    username = request.args.get('username')
    template_string = f"<p>Bonjour {username}</p>"