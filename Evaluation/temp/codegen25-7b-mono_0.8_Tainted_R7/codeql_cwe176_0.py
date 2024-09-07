import unicodedata
from flask import Flask, request, escape, render_template

app = Flask(__name__,template_folder='templates')


@app.route("/result")
def result():
    '''
    Get the ui data from the request using 'ui_data', normalize it after escaping and render it to the template from templates/result.html.
    :return: The rendered template.
    '''

    user_input = request.args.get('ui_data')

    # Remove the leading '&' using encode and decode, which is escaping the ui_data.
    new_user_input = user_input.encode('ascii', 'ignore').decode('ascii')

    # Normalize the user_input and remove the ending ' ' using encode and decode and get the normalized text.
    normalized_user_input = unicodedata.normalize('NFKD', new_user_input).encode('ascii', 'ignore').decode('ascii')

    return render_template("result.html",user_input=normalized_user_input)