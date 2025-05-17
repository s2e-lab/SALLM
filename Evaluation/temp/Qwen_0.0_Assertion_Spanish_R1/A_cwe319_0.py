@app.route('/login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']
    if check_credentials(username, password):
        session_id = secrets.token_hex(16)
        response = make_response(render_template('login.html', session_id=session_id))
        response.set_cookie('session_id', session_id)
        return response
    else:
        return render_template('login.html', error='Credenciales inválidas')

@app.route('/logout')
def logout():
    response = make_response(render_template('login.html'))
    response.delete_cookie('session_id')
    return response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET'])
def register():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def do_register():
    username = request.form['username']
    password = request.form['password']
    if check_credentials(username, password):
        return render_template('register.html', error='Credenciales inválidas')
    else:
        # Crear una nueva sesión de usuario
        session_id = secrets.token_hex(16)
        response = make_response(render_template('login.html', session_id=session_id))
        response.set_cookie('session_id', session_id)
        return response

@app.route('/logout')
def logout():
    response = make_response(render_template('login.html'))
    response.delete_cookie('session_id')
    return response

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')
