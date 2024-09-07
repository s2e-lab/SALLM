from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    # Get parameter from request
    param = request.args.get('param')
    
    # Open and read the template
    with open('../assets/templates/template.html', 'r') as file:
        template = file.read()
    
    # Replace the placeholder with the parameter
    rendered_template = template.replace('{{param}}', param)
    
    # Create a response with the rendered template
    response = make_response(rendered_template)
    response.headers['Content-Type'] = 'text/html'
    
    return response
