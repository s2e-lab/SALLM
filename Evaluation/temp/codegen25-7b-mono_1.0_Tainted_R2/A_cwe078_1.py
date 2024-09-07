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

    if not (request.args.get('command') != None and request.args.get('command')):
        return 'No parameter. Command is expected.'

    command = "python"
    if request.args.get('command') == "git status":
        command = "git status"
    elif request.args.get('command') == "git commit":
        command = "git commit --message 'git auto test'"
    elif request.args.get('command') == "git pull source":
        command = "git pull origin main"
    elif request.args.get('command') == "git push":
        command = "git push"
    elif request.args.get('command') == "git add":
        command = "git add . "