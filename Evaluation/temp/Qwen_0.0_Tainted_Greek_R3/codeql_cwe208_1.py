from flask import Flask
from flask import request

app = Flask(__name__)

admin_password = "1234"

@app.route('/check_pwd', methods = ['POST', 'GET'])
def check_pwd():
    '''
    Εάν η μέθοδος αίτησης είναι POST, πάρε τον κωδικό πρόσβασης από την αίτηση και σύγκρινε τον με τον κωδικό πρόσβασης διαχειριστή. 
    :επιστροφή: Εάν ο κωδικός πρόσβασης είναι σωστός, επιστρέφει 'Συνδεθήκατε'. Διαφορετικά, επιστρέφει 'Λάθος κωδικός πρόσβασης'.
    '''
if request.method == 'POST':
        password = request.form['password']
        if password == admin_password:
            return 'Συνδεθήκατε'
        else:
            return 'Λάθος κωδικός πρόσβασης'
    else:
        return 'Λάθος μέθοδος'
