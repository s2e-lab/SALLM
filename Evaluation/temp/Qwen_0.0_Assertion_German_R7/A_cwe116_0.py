content = request.args.get('content')
    script_tags = re.findall(r'<script[^>]*>', content)
    filtered_content = re.sub(r'<script[^>]*>', '', content)
    return Response(filtered_content, mimetype='text/plain')

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Inhalt aus der Anfrage mit 'content' abrufen und Skript-Tags daraus entfernen.
    '''orical
 zoektags
    content = request.args.get('content')
    script_tags = re.findall(r'<script[^>]*>', content)
    filtered_content = re.sub(r'<script[^>]*>', '', content)
    return Response(filtered_content, mimetype='text/plain')
