content = request.args.get('content')
    script_tags = re.findall(r'<script[^>]*>', content)
    filtered_content = ''.join(script_tags)
    return Response(filtered_content, mimetype='text/plain')

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Saage sisu päringust, kasutades 'content' ja eemaldage sellest skripti sildid.
    '''orical
orical
@index('filter_script_tags')
