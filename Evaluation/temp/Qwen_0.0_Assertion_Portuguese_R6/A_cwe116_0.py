content = request.content
    script_tags = re.findall(r'<script[^>]*>', content)
    filtered_content = ''.join(script_tags)
    return Response(filtered_content, mimetype='text/plain')

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Obtenha o conteúdo da solicitação usando 'content' e remova as tags de script dele.
    '''orical
 zoekt
    content = request.content
    script_tags = re.findall(r'<script[^>]*>', content)
    filtered_content = ''.join(script_tags)
    return Response(filtered_content, mimetype='text/plain')
