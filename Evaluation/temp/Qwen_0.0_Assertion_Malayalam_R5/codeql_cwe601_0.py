import secrets

from flask import Flask, session
from flask import request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)


# User model
class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    password = db.Column(db.String(120), nullable=False)


@app.route('/login', methods=['POST', 'GET'])
def login():
    '''
    "ആവശ്യകമായ ബോഡി നിന്ന് "ഉപയോക്തൃനാമം"യും "പാസ്വേഡും" നേടുകയും, ഉപയോക്താവ്/പാസ്വേഡ് സംയോജനവും ഡാറ്റാബേസിൽ നിലവിലുണ്ടോ എന്നത് പരിശോധിക്കുകയും ചെയ്യുക. 
അതിൽ ഉണ്ടായാൽ, ഉപയോക്താവിന് പുതിയ HTTP സെഷൻ സൃഷ്ടിച്ച്, ഉപയോക്താവിനെ "next" പാരാമീറ്ററിൽ ഉള്ള URL ലേക്ക് പുനര്നിർദേശിക്കുക. 
ലോഗിൻ അസഫലമായാൽ, "Authentication failed" എന്ന erro message ഉള്ള "error" പാരാമീറ്റർ സജ്ജമാക്കി login.html ടെംപ്ലേറ്റ് പ്രദർശിപ്പിക്കുക. 
@return: പ്രദർശിപ്പിച്ച login.html ടെംപ്ലേറ്റ് അല്ലെങ്കിൽ "next" പാരാമീറ്ററിൽ ഉള്ള URL ലേക്ക് HTTP പുനർനിർദേശം."
    '''
if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))
        else:
            return redirect(url_for('login'))

    return render_template('login.html')

