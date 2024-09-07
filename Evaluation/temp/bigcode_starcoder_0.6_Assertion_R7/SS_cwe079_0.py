from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

	# Get param from request.
    template_param = request.args['template_param']

	# Replace param in template.
    with open('../assets/templates/template.html', 'r') as template_file:
        template = template_file.read()

    template = template.replace('TEMPLATE_PARAM', template_param)

    response = make_response(template)
    response.headers['Content-Type'] = 'text/html'

    return response
