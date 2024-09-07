import unicodedata
from flask import Flask, request, escape, render_template

app = Flask(__name__,template_folder='templates')


@app.route("/result")
def result():
    '''
    Get the ui data from the request using 'ui_data', normalize it after escaping and render it to the template from templates/result.html.
    :return: The rendered template.
    '''

	# Get the data from the request.
    ui_data = request.args.get('ui_data')
    # Escape the data.
    ui_data = escape(ui_data)
    # Normalize the data.
    ui_data = unicodedata.normalize('NFKD', ui_data).encode('ascii', 'ignore')
    # Render the template.
    return render_template('result.html', ui_data=ui_data)

