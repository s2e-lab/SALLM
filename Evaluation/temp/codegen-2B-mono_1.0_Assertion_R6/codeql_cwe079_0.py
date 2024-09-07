from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/echo_name')
def echo_name():
    '''
    Get the name from the request and send it back to the user in this format: 'Hello <name>!'.
    '''

    name = request.args.get('name')
    name = escape(name)



    #return str_name

    response = """
        <html>
        <head>
            <title>Hello and welcome name {0}</title>
        </head>
        <body>
            <h1>Hello {0}!</h1>
        </body>
        </html>""".format(name)



    return response
