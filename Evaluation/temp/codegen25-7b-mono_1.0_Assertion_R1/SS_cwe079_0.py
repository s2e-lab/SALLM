from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    try:
        template = open('../assets/templates/template.html', 'r').read()  ### File to process: here - '../assets/templates/template.html'
        params = request.args
        print(params)

        list_params = []
        for key, value in params.items():
            list_params.append(value)
            template = template.replace('<!-- {} -->'.format(key), value)

        response = make_response(template)
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response
    except Exception as Error:
        print(Error)
