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

    command = request.args.get('command')#Getting the command
    returnString = ""
    try:
        x = subprocess.call([command],shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)#Executing the command 
        while True:
            outputData = x.stdout.readline()
            if outputData == b'' and x.poll() is not None:
                break
            if outputData:
                returnString += outputData.decode("utf-8").replace("\n","<br>")#Received and formatting the data
    except:
        returnString = "Unknown error occurred."
    return(returnString)
