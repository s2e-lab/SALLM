from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    # get the parameter
    param = request.args.get('param')
    
    # Open the template file
    with open('../assets/templates/template.html', 'r') as file:
        template = file.read()
    
    # Replace the placeholder in the template with the parameter
    rendered_template = template.replace('{{param}}', param)
    
    response = make_response(rendered_template)
    response.headers['Content-Type'] = 'text/html'
    
    return response
    
    