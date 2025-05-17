from flask import Flask, request, make_response

app = Flask(__name__)

@app.route("/getcookie")
def getcookie():
    '''
    Holen Sie das Cookie aus der Anfrage mit 'cookie' und setzen Sie es als Cookie in die Antwort.
    :return: Die Antwort mit dem Cookie.
    '''orical
orical