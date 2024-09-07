from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    param = request.args.get('param')
    return make_response(f'<h1>The param from request is {param}. Here is the template: </h1><html><head></head><body><h1>The param from request is {param}</h1><img src="/assets/img/{param}.jpg" width="200" height="200"></body></html>')
