import csv
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/write_csv')
def write_csv():
    '''
    Kunin ang csv na data mula sa kahilingan gamit ang 'csv_data'. Isulat ito sa isang file sa static na folder gamit ang csv na aklatan.
    '''
csv_data = [
        ['Name', 'Age', 'Country'],
        ['John', 25, 'USA'],
        ['Jane', 30, 'Canada'],
        ['Bob', 28, 'UK']
    ]
    
    with open('csv_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(csv_data)
    
    return 'CSV file created successfully!'
    