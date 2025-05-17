@app.route('/login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']
    if check_credentials(username, password):
        response = make_response(render_template('login_success.html'))
        response.set_cookie('user_id', username)
        return response
    else:
        return render_template('login_failed.html')

@app.route('/logout')
def logout():
    response = make_response(render_template('logout.html'))
    response.delete_cookie('user_id')
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
        return render_template('register_success.html')
    else:
        return render_template('register_failed.html')

@app.route('/logout')
def logout():
    response = make_response(render_template('logout.html'))
    response.delete_cookie('user_id')
    return response

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')
