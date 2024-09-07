from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''

#     try:
#         first_name = request.args['first_name']
#         msg = 'Greetings, {}!</br><img src="https://lh6.googleusercontent.com/-b0-k99FZlyE/AAAAAAAAAAI/AAAAAAAAAAA/eu7opA4byxI/photo.jpg" width="200" height="113">'.format(escape(first_name))
#     except:
#         msg =  'Please specify a first name.'
    
    first_name = request.args['first_name']
    msg = 'Greetings, {}!</br><img src="https://lh6.googleusercontent.com/-b0-k99FZlyE/AAAAAAAAAAI/AAAAAAAAAAA/eu7opA4byxI/photo.