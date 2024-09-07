import subprocess
import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    '''
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    '''

    command = 'date -u s'
    return subprocess.check_output(command, shell=True, universal_newlines=True)



# @app.route('/create_app_dir')
# def create_app_dir():
#     '''
#     Initialises a new app from a template directory.
#     The template directory can be found in the app_template directory.
#     '''
#     try:
#         # create the app directory in current working directory
#         new_app_dir = './app_{}'.format(random())
#         os.mkdir(new_app_dir)
#
#     finally:
#         # close all subprocesses regardless of exception
#         for process in psutil.Process():
#            