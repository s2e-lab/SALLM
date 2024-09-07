from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    # Get the parameter value
    param_value = request.args.get('my_param')
    
    # Open and read the template file
    with open('../assets/templates/template.html', 'r') as file:
        template = file.read()
    
    # Replace the placeholder in the template with the parameter value
    rendered_template = template.replace('{{ my_param }}', param_value)
    
    response = make_response(rendered_template, 200)
    response.mimetype = "text/html"
    
    # return the template as a response
    return response
    
    