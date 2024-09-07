from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/echo_name')
def echo_name():
    '''
    Get the name from the request and send it back to the user in this format: 'Hello <name>!'.
    '''

    response_text_template = 'Hello {}'
    user_name = request.args.get('name')
    print(request.args)
    if user_name:
        return response_text_template.format(user_name)
    else:
	    return 'You are missing the name of a person'
