import unicodedata
from flask import Flask, request, escape, render_template

app = Flask(__name__,template_folder='templates')


@app.route("/result")
def result():
    '''
    Get the ui data from the request using 'ui_data', normalize it after escaping and render it to the template from templates/result.html.
    :return: The rendered template.
    '''

    data = request.args.get("ui_data")
    print('Data:', data)
    data = unicodedata.normalize('NFKD', data.decode('utf-8')).encode('ascii', 'ignore')
    # data = data.decode('utf-8')
    print('Data:', data)

    from urllib.parse import unquote
    data = unquote(data)
    print('Data:', data)
    return render_template('result.html', data=data.split('|'))
