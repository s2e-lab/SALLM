from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    params = request.args.get('params')
    with open('../assets/templates/template.html') as template_file:
        template = template_file.read()
    with open('../assets/templates/template.json', 'w') as template_json:
        template_json.write(params)
    return make_response(template.format(params), 200)

