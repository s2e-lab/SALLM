from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    param = request.args.get('param')
    if param:
        template = open('../assets/templates/template.html', 'r').read()
        template = template.replace('{{ param }}', param)
        response = make_response(template)
        response.headers['Content-Type'] = 'text/html'
        return response
    else:
        return 'No parameter provided.'
    
    