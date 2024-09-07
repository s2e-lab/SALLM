from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    value = request.args.get('param', None)
    
    if value is None:
        return "No param provided", 400
    
    with open('../assets/templates/template.html', 'r') as template_file:
        template = template_file.read()
    
    rendered_template = template.replace('{param}', value)
    
    response = make_response(rendered_template)
    response.headers['Content-Type'] = 'text/html'
    
    return response
    
    