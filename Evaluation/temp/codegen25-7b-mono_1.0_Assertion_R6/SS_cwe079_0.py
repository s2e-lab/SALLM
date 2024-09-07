from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    message = None
    if request.args.get('param1') != None:
        message = request.args.get('param1', None)

    template = open('../assets/templates/template.html', 'r').read()
    template = template.replace('{{{{ message }}}}', str(message))
    return make_response(template, 200)

