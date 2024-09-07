from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    # get the parameter from the request
    param = request.args.get('param')
    
    # open the template file
    with open('../assets/templates/template.html', 'r') as file:
        # read the file content
        content = file.read()
    
    # replace the placeholder in the template with the param
    content = content.replace('<!-- param -->', param)
    
    # create a response with the rendered template
    response = make_response(content)
    
    return response
    
    # to run the flask app
    