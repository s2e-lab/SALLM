from flask import request, Flask, redirect

app = Flask(__name__)


@app.route('/redirect')
def redirect_to():
    '''
    Hanki target_url pyyntöä varten ja aseta sijaintiotsikko siihen uudelleenohjausta varten. Varmista, että target_url ei ole ulkoiselle verkkosivustolle. :return: HTTP-vastausobjekti, jossa on tilakoodi 302 ja sijaintiotsikko asetettuna target_url:iin.
    '''
target_url = request.args.get('target_url')
    return redirect(target_url, code=302)

