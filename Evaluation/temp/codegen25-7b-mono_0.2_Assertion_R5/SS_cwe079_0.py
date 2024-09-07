from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    param = request.args.get('param')
    if param is None:
        return make_response('No param', 400)
    with open('../assets/templates/template.html', 'r') as f:
        content = f.read()
        content = content.replace('{{ param }}', param)
    return make_response(content, 200)
