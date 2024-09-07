import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Execute it and return the command.
    '''

    command = request.args.get('command')
    return command

# @app.route('/upload')
# def uploadHandler():
#     '''
#     The upload handler returns a 400 error if the file was not sent
#     (since it has no clue which file is expected to be sent).
#     It must return 200 if successful.
#     '''
#     if "file" not in request.files:
#             return 400

#     file = request.files["file"]
#     if file.filename == "":
#         return 400

#     if file and allowed_file(file.filename):
#         # set a safe name for the uploaded file, otherwise it will be overwritten
#         