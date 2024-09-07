from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    template_path = '../assets/templates/template.html'
    param = request.args.get('param')
    
    with open(template_path, 'r') as f:
        file_data = f.read()
    
    replaced_data = file_data.replace('{{ param }}', param)
    
    response = make_response(replaced_data)
    response.headers['Content-Type'] = 'text/html'
    
    return response
    
    