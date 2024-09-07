from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''

    # Using get() to get the value as follows:
    # https://www.w3schools.com/python/ref_string_get.asp
    first_name = request.args.get('first_name')
    if not first_name:
        first_name = "My First Name"
    resp= make_response(f'Hello, {escape(first_name)}!')
    #resp.set_cookie('first_name', first_name, max_age=60*30)
    resp.set_cookie('first_name', 'My First Name', expires=1)
    return resp
