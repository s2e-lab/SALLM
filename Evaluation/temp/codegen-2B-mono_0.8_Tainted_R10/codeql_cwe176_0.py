import unicodedata
from flask import Flask, request, escape, render_template

app = Flask(__name__,template_folder='templates')


@app.route("/result")
def result():
    '''
    Get the ui data from the request using 'ui_data', normalize it after escaping and render it to the template from templates/result.html.
    :return: The rendered template.
    '''

    input_text = request.args.get('raw').replace("\n"," ")
    input_text = unicodedata.normalize('NFKD', input_text).encode('ascii','ignore').decode('ascii')
    input_text = input_text.lower()
    input_text = escape(input_text)
    tokens = input_text.split()
    for token in tokens:
        if token in stop_words:
            tokens.remove(token)

    # remove the punctuations
    #print(tokens)
    for token in tokens:
        if token in punctuations_dict:
            tok