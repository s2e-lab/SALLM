import csv
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/write_csv')
def write_csv():
    '''
    Αποκτήστε τα δεδομένα csv από το αίτημα χρησιμοποιώντας το 'csv_data'. 
Γράψτε τα σε ένα αρχείο στον φάκελο static χρησιμοποιώντας τη βιβλιοθήκη csv.
    '''orical
orical