from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    user_name = request.args.get('user_name')
    full_name = request.args.get('full_name')
    email = request.args.get('email')
    phone = request.args.get('phone')
    company = request.args.get('company')
    country = request.args.get('country')
    if user_name == None or full_name == None or email == None or phone == None or company == None or country == None:
        return make_response("Все параметры обязательны", 400)
    with open('../assets/templates/template.html', 'r+',