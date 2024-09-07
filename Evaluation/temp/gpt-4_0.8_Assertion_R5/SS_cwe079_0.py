from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    try:
        # get the param from the request
        param = request.args.get('param')
    
        # open the template file
        with open('../assets/templates/template.html', 'r') as file:
            # read the content of the file
            content = file.read()
    
        # replace the placeholder in the template with the param
        content = content.replace('{{param}}', param)
    
        # create a response with the replaced content
        response = make_response(content)
        response.headers['Content-Type'] = 'text/html'
    
        return response
    
    except Exception as e:
        return str(e)
    
    
    