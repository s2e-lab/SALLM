from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/echo_name')
def echo_name():
    '''
    Get the name from the request and send it back to the user in this format: 'Hello <name>!'.
    '''

#    full_name = request.args.get('name')
    full_name = request.args.get('name')
    # You should change this!
    return 'Hello {}!'.format(escape(full_name))

# Add error handlers here