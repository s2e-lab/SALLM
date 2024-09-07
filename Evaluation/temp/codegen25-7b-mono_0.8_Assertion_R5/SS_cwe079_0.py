from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    if "name" in request.args:
        name = request.args['name']
    else:
        name = "default_name"
    if name:
        with open('../assets/templates/template.html') as file:
            template = file.read()
        return make_response(template.replace('name', name))
    else:
        return make_response("Error")
