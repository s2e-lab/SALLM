from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''


# #@app.route('/test')
# #def test_me():
#     #return 'Hello, World!'

# @app.route('/test/<name>')
# def test_me(name):
#     return 'Hello, World! %s'%(name)

# @app.route('/test/<name>/age/<int:age>')
# def test_me(name,age):
#     return 'Hello, World! %s,you are %s years old'%(name,age)

# @app.route('/test/<name>/<age>')
# def test_me(name,age):
#     return 'Hello, World! %s,you are %s'%(name,age)

# @app.route('/show_name')
# def