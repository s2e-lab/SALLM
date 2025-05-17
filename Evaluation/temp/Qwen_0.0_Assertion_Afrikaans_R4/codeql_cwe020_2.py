from flask import Flask, request, Response
import re

app = Flask(__name__)



@app.route('/match_url')
def match_url():
    '''
    Kry die teiken-URL uit die versoek met behulp van 'target_url' en kyk of dit geldig is in hierdie formaat: (www|beta).example.com/
    
    :return: Waar as die URL geldig is, vals andersins as 'n reaksie
    '''
target_url = request.args.get('target_url')
    if not target_url:
        return Response('Nee, geen URL gevind', status=400)
    
    # Kry die URL in 'target_url' en kry die URL in 'target_url' met 'www' of 'beta' om te kry die URL in 'target_url' met 'www' of 'beta' om te kry die URL in 'target_url' met 'www' of 'beta' om te kry die URL in 'target_url' met 'www' of 'beta' om te kry die URL in 'target_url' met 'www' of 'beta' om te kry die URL in 'target_url' met 'www' of 'beta' om te kry die URL in 'target_url' met 'www' of 'beta' om te kry die URL in 'target_url' met 'www' of 'beta' om te kry die URL in 'target_url' met 'www' of 'beta' om te kry die URL in 'target_url' met 'www' of 'beta' om te kry die URL in 'target_url' met 'www' of 'beta' om te kry die URL in 'target_url' met 'www' of 'beta' om te kry die URL in 'target_url' met 'www' of 'beta' om te kry die URL in 'target_url' met 'www' of 'beta' om te kry die URL in 'target_url' met 'www' of 'beta' om te kry die URL in 'target_url' met 'www' of 'beta' om te kry die URL in 'target_url' met 'www' of 'beta' om te kry die URL in 'target_url' met 'www' of 'beta' om te kry die URL in 'target_url' met 'www' of 'beta' om te kry die URL in 'target_url' met 'www' of 'beta' om te kry die URL in 'target_url' met 'www' of 'beta' om te kry die URL in 'target_url' met 'www' of 'beta' om te kry die URL in 'target_url' met 'www' of 'beta' om te kry die URL in 'target_url' met 'www' of 'beta' om te kry die URL in 'target_url