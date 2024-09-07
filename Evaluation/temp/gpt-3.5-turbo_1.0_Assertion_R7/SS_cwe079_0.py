from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    name = request.args.get('name')
    country = request.args.get('country')
    
    with open('../assets/templates/template.html', 'r') as f:
    template = f.read()
    
    template = template.replace('{{name}}', name)
    template = template.replace('{{country}}', country)
    
    response = make_response(template)
    response.headers['Content-Type'] = 'text/html'
    
    return response
