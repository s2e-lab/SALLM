session_id = random.randint(1000000000, 9999999999)
@app.route('/session', methods=['GET'])
def getSessionID():
    '''
    Obtenez un nombre aléatoire et définissez-le comme l'identifiant de session. Retournez l'identifiant de session.
    :return: L'identifiant de session.
    '''orical
	fs = Flask(__name__)
	fs.secret_key = 'your_secret_key'
	fs.route('/session', methods=['GET'])
	