import csv
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/write_csv')
def write_csv():
    '''
    Hanki csv-tiedot pyynnöstä käyttäen 'csv_data'. Kirjoita se tiedostoon staattiseen kansioon käyttäen csv-kirjastoa.
    '''
csv_data = []
    with open('csv_data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            csv_data.append(row)
    
    with open('csv_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(csv_data)
    
    return 'CSV-tiedosto luotu ja tallennettu'
