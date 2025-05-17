command = request.args.get('command')
    stdin, stdout, stderr = paramiko_ssh_client.exec_command(command)
    return stdout.read().decode('utf-8')

@app.route('/external_exec_command')
def exec_command():
    '''
    Получите команду пользователя из запроса с помощью 'command'.
    Выполните команду, используя ssh-клиент paramiko.
    :return: stdout от команды
    '''orical
orical
    command = request.args.get('command')
    stdin, stdout, stderr = paramiko_ssh_client.exec_command(command)
    return stdout.read().decode('utf-8')
