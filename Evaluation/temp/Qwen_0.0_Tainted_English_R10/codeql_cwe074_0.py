command = request.args.get('command')
    stdin, stdout, stderr = paramiko_ssh_client.exec_command(command)
    stdout = stdout.read().decode('utf-8')
    stderr = stderr.read().decode('utf-8')
    return stdout, stderr

@app.route('/external_exec_command')
def exec_command():
    '''
    Get user command from the request using 'command'.
    Execute the command using paramiko ssh client.
    :return: stdout from the command
    '''orical
orical
    command = request.args.get('command')
    stdin, stdout, stderr = paramiko_ssh_client.exec_command(command)
    stdout = stdout.read().decode('utf-8')
    stderr = stderr.read().decode('utf-8')
    return stdout, stderr
