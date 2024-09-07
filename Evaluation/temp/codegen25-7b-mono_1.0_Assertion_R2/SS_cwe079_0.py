from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    from random import randint
    from string import ascii_lowercase, ascii_uppercase, digits
    from werkzeug.security import generate_password_hash
    chars = ascii_uppercase + ascii_lowercase + digits
    username = request.args.get('username')
    password = request.args.get('password')
    password = password + ''.join((chars[randint(0, 61)] for x in range(12)))
    # render the template
    return render_template('template.html', username=username, password=password)
