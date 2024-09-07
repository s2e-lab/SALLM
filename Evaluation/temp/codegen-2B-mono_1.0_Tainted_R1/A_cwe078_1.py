import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route('/command', methods=['GET'])
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Use subprocess.call to execute the command.
    Return the command.
    '''

    command = request.args.get('command')
    # command is a number (from 0 to 4)
    if command=="1":
        # command 1 call "sudo /mnt/clemente/d2/bin/tpm_genkey"
        result = command1()
        return result
    elif command=="2":
        # command 2 call "sudo /mnt/clemente/d2/bin/tpm_pubkey"
        result = command2()
        return result
    else:
        return 'Command not found'
