from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    if request.args:
        param = request.args.get('param')
        with open('../assets/templates/template.html', 'r') as f:
            template = f.read()
        template = template.replace('[PARAM]', param)
        return make_response(template)
    else:
        return make_response('No param received.')
