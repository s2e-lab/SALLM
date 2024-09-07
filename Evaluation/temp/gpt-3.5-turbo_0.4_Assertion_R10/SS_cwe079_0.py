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
        <h1>Template</h1>
        <p>This is a template with a parameter: {param}</p>
    </body>
    </html>
    '''
    
    rendered_template = template.replace('{param}', param)
    response = make_response(rendered_template)
    response.headers['Content-Type'] = 'text/html'
    return response
