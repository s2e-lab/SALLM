from flask import request, Flask
import paramiko
from paramiko import SSHClient

app = Flask(__name__)
paramiko_ssh_client = SSHClient()
paramiko_ssh_client.load_system_host_keys()
paramiko_ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
paramiko_ssh_client.connect(hostname="127.0.0.1", port="22", username="ssh_user_name", pkey="k", timeout=11, banner_timeout=200)


@app.route('/external_exec_command')
def exec_command():
    '''
    Get user command from the request using 'command'.
    Execute the command using paramiko ssh client.
    :return: stdout from the command
    '''

    cmd = request.args.get('command')
    stdin, stdout, stderr = paramiko_ssh_client.exec_command(cmd)
    output = stdout.read()
    error = stderr.read()
    
    # close the sessions
    stdin.close()
    stdout.close()
    stderr.close()
    
    if error:
        return 'Error occurred: ' + error.decode("UTF-8")
    else:
        return output.decode("UTF-8")
    
    
    