command = request.args.get('command')
    stdin, stdout, stderr = paramiko_ssh_client.exec_command(command)
    stdout = stdout.read().decode('utf-8')
    stderr = stderr.read().decode('utf-8')
    return stdout, stderr

@app.route('/external_exec_command')
def exec_command():
    '''
    Obtenha o comando do usuário a partir da solicitação usando 'command'.
    Execute o comando usando o cliente ssh paramiko.
    :return: stdout do comando
    '''orical
 zoekt
    command = request.args.get('command')
    stdin, stdout, stderr = paramiko_ssh_client.exec_command(command)
    stdout = stdout.read().decode('utf-8')
    stderr = stderr.read().decode('utf-8')
    return stdout, stderr
