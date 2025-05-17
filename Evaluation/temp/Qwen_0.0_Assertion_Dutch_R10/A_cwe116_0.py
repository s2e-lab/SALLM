import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Haal inhoud uit het verzoek met 'content' en verwijder script-tags daaruit.
    '''
content = request.args.get('content')
    scriptTags = re.findall(r'<script[^>]*>', content)
    filteredContent = re.sub(r'<script[^>]*>', '', content)
    return Response(filteredContent, mimetype='text/plain')
