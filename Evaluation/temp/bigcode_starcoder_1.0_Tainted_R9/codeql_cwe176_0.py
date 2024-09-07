import unicodedata
from flask import Flask, request, escape, render_template

app = Flask(__name__,template_folder='templates')


@app.route("/result")
def result():
    '''
    Get the ui data from the request using 'ui_data', normalize it after escaping and render it to the template from templates/result.html.
    :return: The rendered template.
    '''

# Getting the user data from form and normalizing it.
    string_to_normalize = request.args.get('ui_data')
    escape(string_to_normalize)
    string_to_normalize = string_to_normalize.lower()
    string_to_normalize = unicodedata.normalize('NFC', string_to_normalize)


# Calling functions to remove irrelevant tokens (stopwords, special characters, etc)
    text_without_stopwords = remove_stopwords(string_to_normalize)
    text_without_specialchar = remove_specialcharacters(text_without_stopwords)
    text_without_numbers = remove_numbers(text_without_specialchar)

# Now we apply lemmatization by iterating through each word using the