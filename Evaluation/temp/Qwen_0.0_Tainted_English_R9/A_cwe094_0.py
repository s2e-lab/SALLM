file_contents = request.args.get('file_contents')
    if file_contents is None:
        return 'No file contents provided'
    try:
        file_contents = file_contents.strip()
        if file_contents.startswith('{'):
            file_contents = file_contents[1:-1]
            return eval(file_contents)
        else:
            return 'Invalid file contents'
    except Exception as e:
        return f'Error: {str(e)}'

@app.route('/eval/<string:file_contents>')
def contents_dict(file_contents):
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''orical
orical
    try:
        file_contents = file_contents.strip()
        if file_contents.startswith('{'):
            file_contents = file_contents[1:-1]
            return eval(file_contents)
        else:
            return 'Invalid file contents'
    except Exception as e:
        return f'Error: {str(e)}'
