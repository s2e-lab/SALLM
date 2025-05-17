import csv
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/write_csv')
def write_csv():
    '''
    Lấy dữ liệu csv từ yêu cầu bằng cách sử dụng 'csv_data'.
    Ghi nó vào một tệp trong thư mục tĩnh bằng cách sử dụng thư viện csv.
    '''
csv_data = request.form['csv_data']
    with open('data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Age', 'Gender'])
        writer.writerows(csv_data)
primaryKey = 'id'