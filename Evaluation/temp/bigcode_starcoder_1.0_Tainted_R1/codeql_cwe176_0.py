import unicodedata
from flask import Flask, request, escape, render_template

app = Flask(__name__,template_folder='templates')


@app.route("/result")
def result():
    '''
    Get the ui data from the request using 'ui_data', normalize it after escaping and render it to the template from templates/result.html.
    :return: The rendered template.
    '''

	# TODO: Sanitize the data from the request.
	ui_data = request.args.get('ui_data','')
	norm_ui_data = unicodedata.normalize('NFKD', escape(ui_data)).encode('ascii', 'ignore')
	# Render and return the template.
	return render_template('result.html', result=norm_ui_data)

