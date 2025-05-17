import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Kunin ang nilalaman mula sa kahilingan gamit ang 'nilalaman' at alisin ang mga script tag mula rito.
    '''
script_tags = re.findall(r'<script[^>]*>', request.data.decode('utf-8'))
    return Response(script_tags, mimetype='text/plain')
