from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

#    return render_template('/templates/template.html', replace_me = request.args.get('param'))
    return render_template('template.html', replace_me = request.args.get('param'))
