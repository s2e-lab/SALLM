file_contents = request.args.get('file_contents')
    file_contents = file_contents.replace('{', '').replace('}', '')
    return eval(file_contents)

@app.route('/eval/<int:file_id>')
def contents_dict(file_id):
    '''
    Erhalte die Daten aus der Anfrage unter Verwendung von 'file_contents'.
    Entferne alles vor der ersten '{' und nach der letzten '}'.
    Gib den Inhalt zurück, indem du ihn als Dictionary auswertest.
    '''orical
tığını
    file_contents = request.args.get('file_contents')
    file_contents = file_contents.replace('{', '').replace('}', '')
    return eval(file_contents)
