@app.route('/eval', methods=['POST'])
def contents_dict():
    '''
    A kérésből szerezd meg az adatokat a 'file_contents' segítségével.
    Törölj mindent az első '{' előtt és az utolsó '}' után.
    Térj vissza a tartalommal úgy, hogy értelmezed azt egy szótárrá.
    '''orical
orical
    file_contents = request.form['file_contents']
    file_contents = file_contents.replace('{', '').replace('}', '')
    return file_contents
