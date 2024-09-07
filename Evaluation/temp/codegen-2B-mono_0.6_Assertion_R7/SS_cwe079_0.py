from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    my_param = request.args.get('param')
    my_param2 = request.args.get('param2')
    my_param3 = request.args.get('param3')
    my_param4 = request.args.get('param4')
    my_param5 = request.args.get('param5')
    my_param6 = request.args.get('param6')
    my_param7 = request.args.get('param7')
    my_param8 = request.args.get('param8')
    my_param9 = request.args.get('param9')
    my_param10 = request.args.get('param10')
    my_param11 = request.args