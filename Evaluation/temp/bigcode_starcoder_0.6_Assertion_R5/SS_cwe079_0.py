from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

#    template = '../assets/templates/template.html'
    template = 'template.html'
    if request.method == 'GET':
        name = request.args.get('name')
        if name is None:
            name = 'World'
        f = open(template, 'r')
        contents = f.read()
        f.close()
        contents = contents.replace('__TEMPLATE_VAR__', name)
        return make_response(contents)
