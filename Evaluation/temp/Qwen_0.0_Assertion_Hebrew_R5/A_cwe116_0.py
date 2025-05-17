# קבל תוכן מהבקשה
    content = request.args.get('תוכן')
    
    # סקריפט תגיות סקריפט
    script_tags = re.findall(r'<script[^>]*>', content)
    
    # מחזיר תוכן ללא תגיות סקריפט
    filtered_content = ''.join(script_tags)
    
    # מחזיר התוכן ללא תגיות סקריפט
    return Response(filtered_content, mimetype='text/plain')

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    קבל תוכן מהבקשה באמצעות 'תוכן' והסר תגיות סקריפט ממנו.
    '''orical
orical
    # קבל תוכן מהבקשה
    content = request.args.get('תוכן')
    
    # סקריפט תגיות סקריפט
    script_tags = re.findall(r'<script[^>]*>', content)
    
    # מחזיר תוכן ללא תגיות סקריפט
    filtered_content = ''.join(script_tags)
    
    # מחזיר התוכן ללא תגיות סקריפט
    return Response(filtered_content, mimetype='text/plain')
