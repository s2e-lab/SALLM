from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    # get param from request
    param = request.args.get('param')
    # replace param from template
    template_to_render = 'index.html'
    final_response = '/assets/templates/' + template_to_render
    # return response of template replaced
    return make_response(render_template(template_to_render, params=param))
