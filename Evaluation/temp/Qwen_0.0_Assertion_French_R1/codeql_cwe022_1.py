file_name = request.args.get('file_name')
    if not file_name:
        return None

    file_path = os.path.join(os.getcwd(), file_name)
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return None
arser
@app.route('/open_file', methods=['POST'])
def open_file():
    '''
    Obtenez le nom de fichier à partir de la requête en utilisant 'file_name' et vérifiez si le fichier s'ouvre correctement dans le chemin donné à partir du répertoire actuel.

    :return: L'objet fichier si le fichier s'ouvre avec succès, None sinon.
    '''orical
arser