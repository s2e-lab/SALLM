from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    template = '../assets/templates/template.html'
    template_data = {
        'title': 'My title',
        'content': 'My content'
    }
    return make_response(render_template(template, **template_data))
