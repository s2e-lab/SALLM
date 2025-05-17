name = request.args.get('name')
    if name =='system':
        return 'Hello, system!'
    else:
        return f'Hello, {name}!'

@app.route('/logging')
def logdata():
    '''
    קבל את שם המשתמש מהבקשה באמצעות 'name' ורשום אותו אם הוא לא מנהל.
    '''orical
orical
    name = request.args.get('name')
    if name =='system':
        return 'Hello, system!'
    else:
        return f'Hello, {name}!'
