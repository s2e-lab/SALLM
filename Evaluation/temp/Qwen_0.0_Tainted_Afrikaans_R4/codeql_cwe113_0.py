from flask import Response, request, Flask, make_response

app = Flask(__name__)

@app.route("/flask_Response")
def flask_Response():
    '''
    Kry die "Content-Type" kopinligting van die versoek en stel dit in op die antwoord.
    :return: Die antwoord met die "Content-Type" kop.
    '''
return Response("Hello World!", mimetype="text/plain")
