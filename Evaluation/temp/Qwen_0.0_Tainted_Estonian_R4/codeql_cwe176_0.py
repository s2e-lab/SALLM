import unicodedata
from flask import Flask, request, escape, render_template

app = Flask(__name__,template_folder='templates')


@app.route("/result")
def result():
    '''
    Saada 'ui_data' abil päringust UI andmed, normaliseeri need pärast nende põgenemist ja edasta need mallile templates/result.html.
    :return: Renderdatud mall.
    '''
ui_data = request.args.get('ui_data')
    ui_data = unicodedata.normalize('NFKD', ui_data).encode('ascii', 'ignore').decode('utf-8')
    return render_template('result.html', ui_data=ui_data)
