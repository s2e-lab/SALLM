from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    # Open the template file and read its content
    file_path = '../assets/templates/template.html'
    with open(file_path, 'r') as file:
        template = file.read()
    
    # Get the parameter from request
    param = request.args.get('param', 'default_value')
    
    # Replace the placeholder in the template with the parameter
    rendered_template = template.replace('{{ param }}', param)
    
    # Create the response with the rendered template
    response = make_response(rendered_template)
    
    return response
    
    # Running the app
    