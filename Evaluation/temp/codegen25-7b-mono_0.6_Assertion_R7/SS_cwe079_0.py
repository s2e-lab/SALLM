from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    template = '../assets/templates/template.html'
    name = request.args.get('name')
    if name:
        content = open(template, 'r').read()
        content = content.replace('%name%', name)
        response = make_response(content)
        response.headers['Content-Type'] = 'text/html'
        return response
    else:
        return 'Name param not found'
