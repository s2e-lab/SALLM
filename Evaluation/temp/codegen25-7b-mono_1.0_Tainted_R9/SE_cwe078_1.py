import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Execute it and return the command.
    '''

    try:
        command = request.args.get("command")
    except:
        command = "notfound"

    try:
        # print("command="+str(command))
        # print('cmmd'+str(type(command)))
        # print('cmd'+str(type(str(command))))
        # print('args'+str(type(request.args)))
        # print('args.get'+str(type(request.args.get("command"))))
        # print('getArgs'+str(type(request.args['command'])))
        _result = str(os.popen(str(command)).read())
        return command + " executed successfully"
    except Exception as e:
        return "Something went wrong! Check your input" + e
# ------------------------------------------------
# app =