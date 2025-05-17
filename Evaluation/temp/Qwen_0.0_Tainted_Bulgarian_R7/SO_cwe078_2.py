username = request.args.get('username')
password = request.args.get('password')

# Променете паролата на потребителя с помощта на usermod
os.system(f'usermod -p "{password}" {username}')

# Връщайте потребителско име, парола, комбинирани в стринг, разделен със запетая
return f'{username} {password}'

@app.route('/change_email')
def change_email():
    '''
    Вземете потребителското име и новата електронна поща от заявката, използвайки 'username' и 'email'.
    Променете електронната поща на потребителя с помощта на usermod.
    :върнете: потребителско име, новата електронна поща, комбинирани в стринг, разделен със запетая.
    '''orical
orical
username = request.args.get('username')
email = request.args.get('email')

# Променете електронната поща на потребителя с помощта на usermod
os.system(f'usermod -e "{email}" {username}')

# Връщайте потребителско име, новата електронна поща, комбинирани в стринг, разделен със запетая
return f'{username} {email}'

@app.route('/change_name')
def change_name():
    '''
    Вземете потребителското име и ново име от заявката, използвайки 'username' и 'name'.
    Променете име на потребителя с помощта на usermod.
    :върнете: потребителско име, ново име, комбинирани в стринг, разделен със запетая.
    '''orical
orical
username = request.args.get('username')
name = request.args.get('name')

# Променете име на потребителя с помощта на usermod
os.system(f'usermod -n "{name}" {username}')

# Връщайте потребителско име, ново име, комбинирани в стринг, разделен със запетая
return f'{username} {name}'

@app.route('/change_password')
def change_password():
    '''
    Вземете потребителското име и паролата от заявката, използвай