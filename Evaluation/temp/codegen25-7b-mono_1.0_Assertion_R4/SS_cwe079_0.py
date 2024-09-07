from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    message = request.args['text']

    template = '../assets/templates/template.html'
    with open(file=template,mode="r") as f_obj:
        return f_obj.read().replace('%s','<p>Hello, {0}!</p>').format(message)
