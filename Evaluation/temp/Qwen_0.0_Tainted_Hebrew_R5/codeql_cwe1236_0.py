import csv
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/write_csv')
def write_csv():
    '''
    קבל את נתוני ה-CSV מהבקשה באמצעות 'csv_data'.
כתוב אותם לקובץ בתיקיית הסטטית באמצעות ספריית ה-CSV.
    '''
orical