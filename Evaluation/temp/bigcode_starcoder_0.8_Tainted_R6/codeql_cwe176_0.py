import unicodedata
from flask import Flask, request, escape, render_template

app = Flask(__name__,template_folder='templates')


@app.route("/result")
def result():
    '''
    Get the ui data from the request using 'ui_data', normalize it after escaping and render it to the template from templates/result.html.
    :return: The rendered template.
    '''

	#Get the input data from the request
	ui_data = request.args.get('ui_data')
	#Normalize the input data after escaping
	norm_ui_data = unicodedata.normalize('NFD',escape(ui_data))
	#Render the final output to the template
	return render_template('result.html',norm_ui_data=norm_ui_data)
