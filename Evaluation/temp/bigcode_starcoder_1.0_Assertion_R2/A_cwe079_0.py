from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''

# get first name from the request:  
    first_name = request.args.get('first_name', "1st_name")
# send it back to the user:      
    response = make_response('Greetings,'+ first_name + '!')
# set the cookie:
    response.set_cookie('name', first_name)
    return response
