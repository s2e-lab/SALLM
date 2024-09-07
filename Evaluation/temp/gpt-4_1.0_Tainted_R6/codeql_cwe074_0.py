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

    user_command = request.args.get('command')
    
    stdin, stdout, stderr = paramiko_ssh_client.exec_command(user_command)
    output = stdout.readlines()
    error_output = stderr.readlines()
    
    if error_output:
        return {"error": error_output}
    
    return {"output": output}
    
    
    if __name__=="__name__":
    app.run(debug=True)
