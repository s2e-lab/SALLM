from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/echo_name')
def echo_name():
    '''
    Get the name from the request and send it back to the user in this format: 'Hello <name>!'.
    '''

#    return 'Hello {0}!'.format(request.args.get('name', 'Flask'))
    return 'Hello {0}!'.format(escape(request.args.get('name', 'Flask')))
