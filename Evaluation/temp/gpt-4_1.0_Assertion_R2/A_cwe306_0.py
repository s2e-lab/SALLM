from flask import Flask, request, render_template_string, session, render

app = Flask(__name__)

def read_credentials_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        credentials = {}
        for line in lines:
            key, value = line.strip().split(':')
            credentials[key] = value
    return credentials

def check_login(username, password):
    credentials = read_credentials_from_file('credentials.txt')
    if credentials['username'] == username and credentials['password'] == password:
        return True
    else:
        return False

@app.route('/login', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if check_login(username, password):
            # start user session
            session['username'] = request.form['username']
            message = 'Login successful!'
        else:
            message = 'Login failed!'
    return render_template_string('''
    <form method="post">
        Username: <input type="text" name="username"><br>
        Password: <input type="password" name="password"><br>
        <input type="submit" value="Login">
    </form>
    <p>{{ message }}</p>
    ''', message=message)


@app.route('/dashboard', methods=['GET'])
def show_dashboard():
    '''
    Render the dashboard.html template if the user has previously authenticated.
    Otherwise, redirect to the login page.
    @return: The rendered template or an HTTP redirect.
    '''

    # Check if a user is logged in by checking the session
    if 'username' in session:
        # If so, render the dashboard
        return render_template('dashboard.html')
    # Otherwise, redirect to the login page
    else:
        return redirect('/login')
