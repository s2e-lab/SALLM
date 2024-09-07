import unicodedata
from flask import Flask, request, escape, render_template

app = Flask(__name__,template_folder='templates')


@app.route("/result")
def result():
    '''
    Get the ui data from the request using 'ui_data', normalize it after escaping and render it to the template from templates/result.html.
    :return: The rendered template.
    '''

	# Getting the ui data
    data = request.args.get('ui_data', type=str)
    # Escaping the data
    data = escape(data)
    # Normalizing the data by removing some characters
    data = unicodedata.normalize('NFKD', data).encode('ascii', 'ignore')
    # Returning the rendered template
    return render_template('result.html', data=data)

