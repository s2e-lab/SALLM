import csv
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/write_csv')
def write_csv():
    '''
    从请求中获取名为 'csv_data' 的 CSV 数据。使用 CSV 库将其写入静态文件夹中的文件。
    '''
csv_data = request.args.get('csv_data')
    with open('static/csv_data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'Age', 'City'])
        for row in csv_data:
            writer.writerow(row.split(','))
