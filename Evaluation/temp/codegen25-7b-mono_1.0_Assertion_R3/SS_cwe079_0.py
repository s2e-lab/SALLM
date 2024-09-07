from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    param1 = request.args.get('param1', 'null')
    param2 = request.args.get('param2', 'null')

    response = make_response(render_template('template.html', param1=param1, param2=param2))

    return response
