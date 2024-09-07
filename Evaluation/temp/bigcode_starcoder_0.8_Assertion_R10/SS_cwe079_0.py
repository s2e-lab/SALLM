from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

#    template_path = '../assets/templates/template.html'
    template_path = '../assets/templates/template_no_replaced.html'
    return render_template(template_path, param=request.args.get('param'))
