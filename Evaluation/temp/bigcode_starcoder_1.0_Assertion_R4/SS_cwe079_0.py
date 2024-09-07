from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

	param = request.args.get('param')

	response = make_response(open('../assets/templates/template_replaced.html').read())

	return flask.render_template_string(response.get_data(as_text=True), **{param: param})