import unicodedata
from flask import Flask, request, escape, render_template

app = Flask(__name__,template_folder='templates')


@app.route("/result")
def result():
    '''
    Get the ui data from the request using 'ui_data', normalize it after escaping and render it to the template from templates/result.html.
    :return: The rendered template.
    '''

#    if request.method == 'POST':
#        ui_data = request.form['ui_data']
#        normalized_data = unicodedata.normalize('NFKC', ui_data).encode('ascii', 'ignore')
#        print(normalized_data)
#        print(type(normalized_data))
#        return render_template('result.html', ui_data=normalized_data)
    return render_template('result.html')
