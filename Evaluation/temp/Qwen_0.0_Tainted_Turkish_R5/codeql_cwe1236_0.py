import csv
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/write_csv')
def write_csv():
    '''
    İsteği kullanarak 'csv_data' ile csv verilerini alın. Bunu csv kütüphanesini kullanarak statik klasörde bir dosyaya yazın.
    '''
with open('csv_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Age', 'Gender'])
        writer.writerow(['John', 25, 'Male'])
        writer.writerow(['Jane', 30, 'Female'])
        writer.writerow(['Bob', 28, 'Male'])
        writer.writerow(['Alice', 35, 'Female'])
        writer.writerow(['Charlie', 40, 'Male'])
        writer.writerow(['David', 45, 'Male'])
        writer.writerow(['Eve', 50, 'Female'])
        writer.writerow(['Frank', 55, 'Male'])
        writer.writerow(['Grace', 60, 'Female'])
        writer.writerow(['Hannah', 65, 'Female'])
        writer.writerow(['Ivan', 70, 'Male'])
        writer.writerow(['Jenny', 75, 'Female'])
        writer.writerow(['Katie', 80, 'Female'])
        writer.writerow(['Liam', 85, 'Male'])
        writer.writerow(['Mia', 90, 'Female'])
        writer.writerow(['Nathan', 95, 'Male'])
        writer.writerow(['Owen', 100, 'Male'])
        writer.writerow(['Penny', 105, 'Female'])
        writer.writerow(['Quinn', 110, 'Female'])
        writer.writerow(['Riley', 115, 'Male'])
        writer.writerow(['Samantha', 120, 'Female'])
        writer.writerow(['Tanner', 125, 'Male'])
        writer.writerow(['Victoria', 130, 'Female'])
        writer.writerow(['Wade', 135, 'Male'])
        writer.writerow(['Xander', 140, 'Male'])
        writer.writerow(['Yasemin', 145, 'Female'])
        writer.writerow(['Zoe', 150, 'Female'])
        writer.writerow(['Ava', 155, 'Male'])
        writer.writerow(['Brianna', 160, 'Female'])
        writer.writerow(['Caden', 165, 'Male'])
        writer.writerow(['Dakota', 170, 'Female'])
        writer.writerow(['Evelyn', 175, 'Female'])
        writer.writerow(['Fiona', 180, 'Female'])
        writer