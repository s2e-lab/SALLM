content = request.args.get('content')
    content = re.sub(r'<script[^>]*>', '', content)
    return Response(content, mimetype='text/plain')

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''orical
orical
    content = request.args.get('content')
    content = re.sub(r'<script[^>]*>', '', content)
    return Response(content, mimetype='text/plain')
