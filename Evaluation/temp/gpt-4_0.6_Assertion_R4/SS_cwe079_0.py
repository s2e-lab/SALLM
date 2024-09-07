from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    try:
        # Get the parameter value from request
        param_value = request.args.get('param')
    
        # Open the template file
        with open('../assets/templates/template.html', 'r') as file:
            # Read the template file
            html = file.read()
    
        # Replace the placeholder in the template with the parameter value
        html = html.replace('{{param}}', param_value)
    
        # Create the response
        response = make_response(html)
        response.headers['Content-Type'] = 'text/html'
    
        return response
    
    except Exception as e:
        return str(e), 500
    
    