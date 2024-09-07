from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    # Read the template
    with open('../assets/templates/template.html', 'r') as file:
        template = file.read()
        
    # Get param from request
    param = request.args.get('param', '')
    
    # replace the placeholder with the actual param
    # assuming that the placeholder is marked as {param} in the template
    rendered_template = template.replace('{param}', param)
    
    # Create response
    response = make_response(rendered_template)
    return response
    
    