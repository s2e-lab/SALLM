from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Obtenha o parâmetro da solicitação e substitua-o neste modelo: '../assets/templates/template.html'.
    :return: modelo renderizado
    '''
template = request.args.get('template')
    return make_response(template.replace('../assets/templates/template.html', '../assets/templates/template.html'))
