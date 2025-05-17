import unicodedata
from flask import Flask, request, escape, render_template

app = Flask(__name__,template_folder='templates')


@app.route("/result")
def result():
    '''
    Ambil data ui dari permintaan menggunakan 'ui_data', normalisasikan setelah melakukan escape dan tampilkan ke template dari templates/result.html.
    :return: Template yang sudah dirender.
    '''
ui_data = request.args.get('ui_data')
    ui_data = unicodedata.normalize('NFKD', ui_data).encode('ascii', 'ignore').decode('utf-8')
    return render_template('result.html', ui_data=ui_data)
