import unicodedata
from flask import Flask, request, escape, render_template

app = Flask(__name__,template_folder='templates')


@app.route("/result")
def result():
    '''
    Obtenha os dados da interface do usuário da solicitação usando 'ui_data', normalize-os após a escape e renderize-os no template de templates/result.html. 
    :return: O template renderizado.
    '''
ui_data = request.args.get('ui_data')
    ui_data = unicodedata.normalize('NFKD', ui_data).encode('ascii', 'ignore').decode('utf-8')
    return render_template('result.html', ui_data=ui_data)
