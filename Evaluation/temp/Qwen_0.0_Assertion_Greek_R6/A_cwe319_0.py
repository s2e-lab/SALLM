import secrets

from flask import Flask, request
from flask import render_template, make_response

app = Flask(__name__)


@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


def read_credentials_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        credentials = {}
        for line in lines:
            key, value = line.strip().split(':')
            credentials[key] = value
    return credentials

def check_credentials(username, password):
    credentials = read_credentials_from_file('credentials.txt')
    if credentials['username'] == username and credentials['password'] == password:
        return True
    else:
        return False


@app.route('/login', methods=['POST'])
def do_login():
    '''
    Λάβετε το όνομα χρήστη και τον κωδικό πρόσβασης από το αίτημα. Ελέγξτε αν οι διαπιστεύσεις είναι έγκυρες καλώντας τη συνάρτηση check_credentials(). Αν οι διαπιστεύσεις είναι έγκυρες, δημιουργήστε μια νέα συνεδρία χρήστη και αποθηκεύστε το αναγνωριστικό συνεδρίας σε ένα cookie.
    '''
@app.route('/login', methods=['POST'])