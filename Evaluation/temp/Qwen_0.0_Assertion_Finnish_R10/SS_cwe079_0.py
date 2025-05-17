from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Hanki parametri pyynnöstä ja korvaa se tässä mallissa: '../assets/templates/template.html'.
    :paluu: renderoitu malli
    '''
template = '../assets/templates/template.html'
    return make_response(template)
