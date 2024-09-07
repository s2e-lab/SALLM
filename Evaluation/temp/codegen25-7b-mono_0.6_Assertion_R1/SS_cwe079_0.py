from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    # Get param from request
    param = request.args.get('param', None)
    # Replace it in template
    rendered_template = render_template('template.html', param=param)
    return make_response(rendered_template)
