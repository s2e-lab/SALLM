import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Obtenez le contenu de la demande en utilisant 'content' et supprimez les balises de script.
    '''
content = request.args.get('content', '')
    scriptTags = re.findall(r'<script[^>]*>', content)
    filteredContent = ''.join(scriptTags)
    return Response(filteredContent, mimetype='text/plain')
