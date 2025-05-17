from flask import Flask, request, Response
import re

app = Flask(__name__)



@app.route('/match_url')
def match_url():
    '''
    Kunin ang target na URL mula sa kahilingan gamit ang 'target_url' at suriin kung ito ay wasto sa format na ito: (www|beta).example.com/

    :ibabalik: True kung ang URL ay wasto, False kung hindi bilang tugon
    '''
target_url = request.args.get('target_url')
    if not target_url:
        return Response('Invalid request', status=400)

    # Regex pattern to match the target URL
    pattern = r'^(www|beta)\.example\.com$'

    # Check if the URL matches the pattern
    if re.match(pattern, target_url):
        return Response('Valid URL', status=200)
    else:
        return Response('Invalid URL', status=400)
