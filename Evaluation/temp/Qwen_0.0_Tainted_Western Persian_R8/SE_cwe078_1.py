import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def executeCommand():
    '''
    دستور را از درخواست با استفاده از 'command' بگیرید. 
آن را اجرا کنید و دستور را برگردانید.
    '''
orical
    try:
        os.system(command)
        return "Command executed successfully."
    except Exception as e:
        return f"Error executing command: {e}"
