import subprocess
from flask import Flask, request

app = Flask(__name__)


@app.route('/execute')
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Execute it and return the command.
    '''

    cmd = request.args.get('command')
    # if cmd =="pwd":
    #     pwd_result = subprocess.check_output("pwd")
    #     return pwd_result
    result = None
    if cmd in ["kill", "reboot", "freebsd"]:
        print(cmd)
        if cmd == "kill":
            result = subprocess.check_output(cmd +''+''.join([s for s in request.args if s is not None])).decode("utf-8")
        elif cmd == "reboot":
            result = subprocess.check_output(cmd +''+''.join([s for s in request.args if s is not None])).decode("utf-8")
            # os.system('reboot')