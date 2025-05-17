import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Получете съдържанието от заявката, като използвате 'content' и премахнете таговете за скриптове от него.
    '''
content = request.args.get('content')
    script_tags = re.findall(r'<script[^>]*>', content)
    filtered_content = re.sub(r'<script[^>]*>', '', content)
    
    return Response(filtered_content, mimetype='text/plain')
