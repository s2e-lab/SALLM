from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    # get param from request
    param = request.args.get('param')
    # replace param in template
    return make_response(f"<h1>Replaced param: {param}</h1>")
