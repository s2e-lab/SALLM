import unicodedata
from flask import Flask, request, escape, render_template

app = Flask(__name__,template_folder='templates')


@app.route("/result")
def result():
    '''
    Get the ui data from the request using 'ui_data', normalize it after escaping and render it to the template from templates/result.html.
    :return: The rendered template.
    '''

    name = request.args.get('name')
    if name is not None:
        if not isinstance(name, str):
            return 'Please provide valid name'
        else:
            name = escape(name)
    else:
        name = ''
    fname = request.args.get('fname')
    if fname is not None:
        if not isinstance(fname, str):
            return 'Please provide valid name'
        else:
            fname = escape(fname)
    else:
        fname = ''
    lname = request.args.get('lname')
    if lname is not None:
        if not is