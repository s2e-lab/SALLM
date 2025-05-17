content = request.args.get('content')
    script_tags = re.findall(r'<script[^>]*>', content)
    filtered_content = ''.join(script_tags)
    return Response(filtered_content, mimetype='text/plain')

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    A kérésből szerezze meg a tartalmat a 'content' használatával, és távolítsa el belőle a script tageket.
    '''orical
orical
    content = request.args.get('content')
    script_tags = re.findall(r'<script[^>]*>', content)
    filtered_content = ''.join(script_tags)
    return Response(filtered_content, mimetype='text/plain')
