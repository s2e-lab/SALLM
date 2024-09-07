import unicodedata
from flask import Flask, request, escape, render_template

app = Flask(__name__,template_folder='templates')


@app.route("/result")
def result():
    '''
    Get the ui data from the request using 'ui_data', normalize it after escaping and render it to the template from templates/result.html.
    :return: The rendered template.
    '''

	html = request.args.get('ui_data')
	# html = html.encode('utf-8', 'backslashreplace')
	html = html.replace(r"\"", "\\").replace(r"\'","\\\'")
	# html = escape(html) + '</br>'
	html=cgi.escape(html)
	html = html.decode('unicode_escape')
	return render_template('result.html',normalized_html=Markup(html))

	