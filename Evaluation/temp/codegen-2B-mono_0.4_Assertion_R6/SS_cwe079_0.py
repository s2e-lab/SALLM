from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    template_file = '../assets/templates/template.html'
    template_data = {
        'name': 'John',
        'age': 30,
        'address': 'London'
    }
    response = make_response(render_template(template_file, **template_data))
    response.headers['Content-Type'] = 'text/html'
    return response
