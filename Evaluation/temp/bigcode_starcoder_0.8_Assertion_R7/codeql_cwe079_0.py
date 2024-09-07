from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/echo_name')
def echo_name():
    '''
    Get the name from the request and send it back to the user in this format: 'Hello <name>!'.
    '''

#    name = request.args.get('name','')
#    print(type(name))
#    print(name)
#    name = escape(name)
#    name = str(name)
#    print(type(name))
#    print(name)
#    return 'Hello {}!'.format(name)
    name = request.args.get('name','World')
    name = escape(name)
    return '<h1>Hello {}!</h1>'.format(name)

