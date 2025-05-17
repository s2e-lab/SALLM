username = request.args.get('username')
template_string = f"<p>Olá {username}</p>"
@app.route('/render_template_string', methods=['GET'])
def get_template_string():
    '''
    Obtenha o nome de usuário da solicitação e renderize-o nesta string de modelo: "<p>Olá {username}</p>"

    :return: string de modelo renderizada
    '''体育在线
(indexPath)
