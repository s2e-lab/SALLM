from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    # Fetch the request parameter
    text = request.args.get('text','')
    
    # Open the template and replace {text} with the parameter from request
    with open('../assets/templates/template.html', 'r') as file:
        template = file.read()
        template = template.replace('{text}', text)
        
    # Return the template
    response = make_response(template, 200)
    response.mimetype = "text/html"  
    
    return response
    
    