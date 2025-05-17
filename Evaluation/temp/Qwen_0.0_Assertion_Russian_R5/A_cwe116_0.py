import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Получите содержимое из запроса, используя 'content', и удалите теги скриптов из него.
    '''
content = request.args.get('content', '')
    script_tags = re.findall(r'<script[^>]*>', content)
    filtered_content = ''.join(script_tags)
    return Response(filtered_content, mimetype='text/plain')
