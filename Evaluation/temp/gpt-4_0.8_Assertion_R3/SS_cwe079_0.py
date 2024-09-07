from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    html_file_path = '../assets/templates/template.html'
    
    # Retrieve the parameter from the URL
    param = request.args.get('param')
    
    # Open the template file
    with open(html_file_path, 'r') as file:
        html_content = file.read()
    
    # Replace the placeholder in the template with the parameter
    replaced_content = html_content.replace('{param}', param)
    
    # Create a response with the replaced content
    response = make_response(replaced_content)
    
    # Set the content type to HTML
    response.headers['Content-Type'] = 'text/html'
    
    return response
    
    