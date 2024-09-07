from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    param = request.args.get('param')
    template = "../assets/templates/template.html"
    with open(template, 'r') as file:
        content = file.read()
    replaced_content = content.replace('<param>', param)
    response = make_response(replaced_content)
    response.headers['Content-Type'] = 'text/html'
    return response
    
    