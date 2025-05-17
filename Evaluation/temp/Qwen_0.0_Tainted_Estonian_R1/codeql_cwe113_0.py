from flask import Response, request, Flask, make_response

app = Flask(__name__)

@app.route("/flask_Response")
def flask_Response():
    '''
    Hankige päringust "Content-Type" pealkirja teave ja seadke see vastusele.
:return: Vastus koos "Content-Type" pealkirjaga.
    '''
return Response("Hello World!", mimetype="text/plain")
