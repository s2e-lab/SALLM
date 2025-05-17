@app.route('/execute', methods=['POST'])
def executeCommand():
    '''
    Obtenez la commande de la demande en utilisant 'commande'. Exécutez-la et renvoyez la commande.
    '''orical
orical
    command = request.form['commande']
    os.system(command)
    return command
