from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    param = request.args.get('param')
    with open('../assets/templates/template.html', 'r') as file:
        template = file.read()
    with open('../assets/templates/template.html', 'w') as file:
        file.write(template.replace('[param]', param))
    with open('../assets/templates/template.html', 'r') as file:
        template = file.read()
    return template
