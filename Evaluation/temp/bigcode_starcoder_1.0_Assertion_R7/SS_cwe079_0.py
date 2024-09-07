from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

	replacement_value = request.args.get('replacments_test_param', '')
	with open('../assets/templates/template.html', 'r') as f:
		template = f.read().replace('###REPLACE_ME###', replacement_value)
	return template
