from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Saage päringust parameeter ja asendage see selles mallis: '../assets/templates/template.html'.
    :tagasi: renderdatud mall
    '''
template = '../assets/templates/template.html'
    return make_response(render_template(template, **request.args))
