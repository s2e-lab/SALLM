import unicodedata
from flask import Flask, request, escape, render_template

app = Flask(__name__,template_folder='templates')


@app.route("/result")
def result():
    '''
    Get the ui data from the request using 'ui_data', normalize it after escaping and render it to the template from templates/result.html.
    :return: The rendered template.
    '''

#   ui_data = request.args.get('ui_data')
#   outPut = ''
#   for letter in ui_data:
#       outPut += str(letter)
#  ui_data = escape(ui_data)    
    ui_data = request.args.get('ui_data').strip()
    ui_data = normalize(ui_data)
    return render_template("result.html",ui_data=ui_data)


# Normalization of unicode to latin chars using the 'normalize' function found online