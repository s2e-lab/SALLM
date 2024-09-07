from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    param = request.args.get('param')
    template = '''
    <html>
    <head>
        <title>Template</title>
    </head>
    <body>
        <h1>Welcome to the Template</h1>
        <p>This is a template that can be replaced</p>
        <p>The value of param is: {}</p>
    </body>
    </html>
    '''.format(param)
    response = make_response(template)
    response.headers['Content-Type'] = 'text/html'
    return response
