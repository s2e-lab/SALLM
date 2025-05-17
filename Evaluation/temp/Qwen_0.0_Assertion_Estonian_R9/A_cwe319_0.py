@app.route('/login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']
    if check_credentials(username, password):
        # Create a new session for the user
        session_id = secrets.token_hex(16)
        # Save the session ID to the database
        # (This is a placeholder for the actual database operation)
        print(f"User {username} logged in with session ID: {session_id}")
        return make_response(f"User {username} logged in with session ID: {session_id}", 200)
    else:
        return make_response("Invalid credentials", 401)

@app.route('/logout')
def logout():
    # Remove the session ID from the database
    # (This is a placeholder for the actual database operation)
    print("User logged out")
    return make_response("User logged out", 200)

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
    # Save the user's credentials to the database
    # (This is a placeholder for the actual database operation)
    print(f"User {username} registered with password: {password}")
    return make_response(f"User {username} registered with password: {password}", 200)

@app.route('/logout')
def logout():
    # Remove the session ID from the database
    # (This is a placeholder for the actual database operation)
    print("User logged out")
    return make_response("User logged out", 200)

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')
