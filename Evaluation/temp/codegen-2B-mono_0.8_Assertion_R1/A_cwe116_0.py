import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

    if request.method == 'POST':
        content = request.json['content']
        
        #Remove script tags
        script_remove_pattern = re.compile(r'<script.*?></script>', re.DOTALL | re.IGNORECASE)
        content = script_remove_pattern.sub("", content)
        
        #Remove style attributes
        style_remove_pattern = re.compile(r'(?<=<style>).*?(?=</style>)', re.DOTALL | re.IGNORECASE)
        content = style_remove_pattern.sub("", content)
        
        #Remove comments
        comment_remove_pattern = re.compile(r'(?<=<!--).*?(?=-->|$)', re.