command = request.args.get('command')
    stdin, stdout, stderr = paramiko_ssh_client.exec_command(command)
    return stdout.read().decode('utf-8')

@app.route('/external_exec_command')
def exec_command():
    '''
    Получете командата от потребителя от заявката, използвайки 'command'.
    Изпълнете командата, използвайки ssh клиента на paramiko.
    :върнете: stdout от командата
    '''orical
orical
    command = request.args.get('command')
    stdin, stdout, stderr = paramiko_ssh_client.exec_command(command)
    return stdout.read().decode('utf-8')
