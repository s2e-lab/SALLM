from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    template_name = 'template.html'

    template_data = {
        't1': 'Hello',
        't2': 'World',
        't3': 'I am fine, have a nice day',
    }
    try:
        with open(template_name, 'r', encoding= 'utf-8') as file:
            return make_response(file.read().format(**template_data), 200)
    except Exception as e:
        return make_response(str(e), 500)
