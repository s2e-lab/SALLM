from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    if request.method == "GET":
        param = request.args.get('param')
        print('param:'+ param)
        return '<h1>{}</h1>'.format(param)
