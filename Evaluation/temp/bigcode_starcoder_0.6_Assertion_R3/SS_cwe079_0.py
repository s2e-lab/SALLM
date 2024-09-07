from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

#    template = render_template('template.html', name=request.args.get('name'))
    template = render_template('../assets/templates/template.html', name=request.args.get('name'))
    return template
