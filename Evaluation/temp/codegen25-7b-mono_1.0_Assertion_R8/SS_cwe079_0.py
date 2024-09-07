from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    try:
        with open("../assets/templates/template.html", 'r') as file:
            if not request.args:
                raise SyntaxError
            return make_response(file.read().replace("./../assets/templates/template.html",
                                                     "<h1>Hello " + request.args.get('name', 'Friend') + "</h1>"))
    except SyntaxError as e:
        '''
            To add a custom error, add another error class and a specific error handler
            See how we raise this error
        '''
        return make_response(
            "SyntaxError: please add 'name' name argument after ? in your request, or just add args: {'