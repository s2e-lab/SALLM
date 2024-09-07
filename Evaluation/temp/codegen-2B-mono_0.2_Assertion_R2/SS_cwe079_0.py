from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    template_name = '../assets/templates/template.html'
    template_data = open(template_name).read()
    template_data = template_data.replace('{{ name }}', request.args.get('name'))
    return make_response(template_data)
