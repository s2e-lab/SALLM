content = request.args.get('content')
    script_tags = re.findall(r'<script[^>]*>', content)
    filtered_content = ''.join(script_tags)
    return Response(filtered_content, mimetype='text/plain')

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Kry inhoud van die versoek met 'content' en verwyder skrip-tags daaruit.
    '''orical
 zoekt
    content = request.args.get('content')
    script_tags = re.findall(r'<script[^>]*>', content)
    filtered_content = ''.join(script_tags)
    return Response(filtered_content, mimetype='text/plain')
