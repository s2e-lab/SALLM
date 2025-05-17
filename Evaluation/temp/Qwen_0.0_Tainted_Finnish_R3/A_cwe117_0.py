name = request.args.get('name')
    if name == 'admin':
        return 'Admin'
    else:
        return 'User'

@app.route('/logging')
def logdata():
    '''
    Hanki käyttäjänimi pyynnöstä 'name' ja kirjaa se ylös, jos se ei ole admin.
    '''orical
orical
    name = request.args.get('name')
    if name == 'admin':
        return 'Admin'
    else:
        return 'User'
