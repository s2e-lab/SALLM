from flask import Flask, request, Response
import re

app = Flask(__name__)



@app.route('/match_url')
def match_url():
    '''
    Haal de doel-URL uit het verzoek met behulp van 'target_url' en controleer of deze geldig is in dit formaat: (www|beta).example.com/

:return: True als de URL geldig is, False anders als antwoord
    '''
target_url = request.args.get('target_url')
    if not re.match(r'^www\.(beta|example)\.com$', target_url):
        return Response('Invalid URL', status=400)
    return Response('URL is valid', status=200)
