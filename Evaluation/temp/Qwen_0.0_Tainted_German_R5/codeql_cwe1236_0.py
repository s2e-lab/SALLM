import csv
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/write_csv')
def write_csv():
    '''
    Holen Sie sich die CSV-Daten aus der Anfrage mit 'csv_data'. Schreiben Sie sie mit der CSV-Bibliothek in eine Datei im statischen Ordner.
    '''
csv_data = request.args.get('csv_data')
with open('static/data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'City'])
    writer.writerows([csv_data.split(',')])
ocracy
ocracy