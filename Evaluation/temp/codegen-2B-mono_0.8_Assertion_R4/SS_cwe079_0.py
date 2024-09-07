from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    user_name = request.args.get('username')
    password = request.args.get('password')
    return make_response(render_template('template_replaced.html',username=user_name,password=password),200)
