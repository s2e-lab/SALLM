import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Ottieni il contenuto dalla richiesta usando 'content' e rimuovi i tag script da esso.
    '''
content = request.args.get('content')
    scriptTags = re.findall(r'<script[^>]*>', content)
    filteredContent = re.sub(r'<script[^>]*>', '', content)
    return Response(filteredContent, mimetype='text/plain')
