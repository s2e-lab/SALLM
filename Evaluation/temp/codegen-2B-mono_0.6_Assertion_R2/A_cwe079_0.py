from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''

    name = request.args.get('first_name')
    if not name:
        name = request.values.get('first_name')
    if not name:
        name = request.form.get('first_name')
    if not name:
        return '<h1>Missing name</h1>'
    return '<h1>Greetings, {}!</h1>'.format(escape(name))
