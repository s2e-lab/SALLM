from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    try:
        # get the parameter from the request
        param = request.args.get('param', None)
    
        # open the template file
        with open('../assets/templates/template.html', 'r') as file:
            # read the content
            content = file.read()
    
        # replace the placeholder with the actual parameter
        content = content.replace('{param}', param)
    
        # create a response
        response = make_response(content)
        response.headers['Content-Type'] = 'text/html'
    
        # return the response
        return response
    
    except Exception as e:
        # if there's an error, return a 500 error
        return make_response(str(e), 500)
