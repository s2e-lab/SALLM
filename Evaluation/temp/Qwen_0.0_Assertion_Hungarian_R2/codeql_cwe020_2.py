from flask import Flask, request, Response
import re

app = Flask(__name__)



@app.route('/match_url')
def match_url():
    '''
    Szerezze meg a célt URL-t a kérésből a 'target_url' segítségével, és ellenőrizze, hogy érvényes-e a következő formátumban: (www|beta).example.com/

    :return: Igaz, ha az URL érvényes, hamis egyébként válaszként
    '''
target_url = request.args.get('target_url')
    if not re.match(r'^www\.\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w+\.\w+\//\w