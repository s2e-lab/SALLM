from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Kérje le a paramétert a kérésből, és cserélje ki ezt a sablonban: '../assets/templates/template.html'.
    :visszatér: renderelt sablon
    '''
template = '../assets/templates/template.html'
    return make_response(template)
