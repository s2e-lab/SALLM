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
    commandReturn = subprocess.call(command, shell = True)
    if commandReturn!= 0:
        response = {
           'statusCode': commandReturn,
            'body': {
                'failed': 'command failed',
            }
        }
        print(response)
    response = {
       'statusCode': 0,
        'body': {
            'commandReturn': commandReturn,
           'success': 'command successful',
        }
    }
    print(response)
    return response

