from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    # Open the template file
    with open('../assets/templates/template.html', 'r') as file:
        template = file.read()
    
    # Get the parameter from the request
    param = request.args.get('param')
    
    # Replace the placeholder in the template with the parameter
    template = template.replace('{{param}}', param)
    
    # Create a response with the rendered template
    response = make_response(template)
    
    return response
    
    