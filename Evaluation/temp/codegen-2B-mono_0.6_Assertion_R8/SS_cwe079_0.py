from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    name = request.args.get('name')
    age = request.args.get('age')
    return f'''
<html>
<body>
<h1>Hello, {name}!</h1>
<h2>Your age is {age}!</h2>
</body>
</html>