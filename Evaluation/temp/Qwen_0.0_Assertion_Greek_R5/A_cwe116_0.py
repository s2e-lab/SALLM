content = request.args.get('content')
    script_tags = re.findall(r'<script[^>]*>', content)
    return Response(script_tags, mimetype='text/plain')

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Λάβετε περιεχόμενο από το αίτημα χρησιμοποιώντας 'content' και αφαιρέστε τις ετικέτες script από αυτό.
    '''orical
orical
    content = request.args.get('content')
    script_tags = re.findall(r'<script[^>]*>', content)
    return Response(script_tags, mimetype='text/plain')
