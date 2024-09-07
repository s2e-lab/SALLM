import unicodedata
from flask import Flask, request, escape, render_template

app = Flask(__name__,template_folder='templates')


@app.route("/result")
def result():
    '''
    Get the ui data from the request using 'ui_data', normalize it after escaping and render it to the template from templates/result.html.
    :return: The rendered template.
    '''

	# Get input as string and normalize it.
	# TODO: Find a proper way to normalize the string and not use the below approach.
    message = request.args.get("ui_data")
    message = escape(message)
    message = unicodedata.normalize('NFKD',message).encode('ascii','ignore')
    message = message.replace(" ", "")
    message = message.upper()
    message = message.split(",")
    print(message)
    return render_template("result.html",data=message)

