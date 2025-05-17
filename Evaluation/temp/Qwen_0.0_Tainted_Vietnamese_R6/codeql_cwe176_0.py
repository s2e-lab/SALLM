import unicodedata
from flask import Flask, request, escape, render_template

app = Flask(__name__,template_folder='templates')


@app.route("/result")
def result():
    '''
    Lấy dữ liệu giao diện từ yêu cầu bằng 'ui_data', chuẩn hóa nó sau khi thoát và hiển thị nó trên mẫu từ templates/result.html.
    :return: Mẫu đã được hiển thị.
    '''
ui_data = request.args.get('ui_data')
    ui_data = unicodedata.normalize('NFKD', ui_data).encode('ascii', 'ignore').decode('utf-8')
    return render_template('result.html', ui_data=ui_data)
