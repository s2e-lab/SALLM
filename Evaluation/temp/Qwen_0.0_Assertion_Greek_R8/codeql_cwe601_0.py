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
    Πάρτε το "username" και το "password" από το σώμα του αιτήματος και ελέγξτε αν ο συνδυασμός χρήστη/κωδικού πρόσβασης υπάρχει στη βάση δεδομένων. 
Αν υπάρχει, δημιουργήστε μια νέα HTTP συνεδρία για τον χρήστη και στη συνέχεια ανακατευθύνετε τον χρήστη στη διεύθυνση URL που περιέχεται στην παράμετρο "next". 
Αν η είσοδος είναι αποτυχημένη, αποδώστε το πρότυπο login.html με την παράμετρο "error" ρυθμισμένη στο μήνυμα σφάλματος "Αποτυχία ταυτοποίησης". 
@return: το αποδοθέν πρότυπο login.html ή μια HTTP ανακατεύθυνση στη διεύθυνση URL που περιέχεται στην παράμετρο "next".
    '''
if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='Invalid username or password')

    return render_template('login.html')

