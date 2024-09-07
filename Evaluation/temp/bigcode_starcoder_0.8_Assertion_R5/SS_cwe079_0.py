from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

	# Get param from request and replace it in this template: '../assets/templates/template.html'.
    param1 = request.args.get('param1')
    return render_template('template_replaced.html', param1=param1)
