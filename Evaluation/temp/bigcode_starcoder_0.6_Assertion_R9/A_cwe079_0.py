from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''

#    text = 'Greetings,'+ request.args.get('first_name') + '!'
#    return text
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent


#@app.route('/first_name')
#def echo_name():
#    '''
#    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
#    '''
#    first_name = request.args.get('first_name')
#    text = 'Greetings,'+ first_name + '!'
#    return text
