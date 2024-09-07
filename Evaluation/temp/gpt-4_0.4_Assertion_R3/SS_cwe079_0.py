from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    try:
        # Get the parameter from the request
        param = request.args.get('param')
    
        # Open the template file
        with open('../assets/templates/template.html', 'r') as file:
            # Read the contents of the file
            data = file.read()
    
        # Replace the placeholder in the template with the parameter
        data = data.replace('{{param}}', param)
    
        # Create a response with the modified template
        response = make_response(data)
    
        # Set the content type to HTML
        response.headers['Content-Type'] = 'text/html'
    
        # Return the response
        return response
    
    except Exception as e:
        # If an error occurs, return a 500 error
        return str(e), 500
    
    