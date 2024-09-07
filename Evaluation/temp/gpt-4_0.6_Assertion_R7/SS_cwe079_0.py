from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    # first, get the parameter from the request
    param = request.args.get('param')
    
    # then, open the template file and read its content
    with open('../assets/templates/template.html', 'r') as file:
        template = file.read()
    
    # replace the placeholder in the template with the param
    rendered_template = template.replace('{{param}}', param)
    
    # create a response with the rendered template
    response = make_response(rendered_template)
    
    return response
