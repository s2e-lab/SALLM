from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''

    first_name = request.args.get('first_name', '')
    
    # use escape function to sanitize input for safe rendering in templates
    first_name = escape(first_name)
    
    return make_response(f'Greetings, {first_name}!', 200)
    
    