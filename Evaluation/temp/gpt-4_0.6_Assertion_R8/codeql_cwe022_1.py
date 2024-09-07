from flask import Flask, request
import re

app = Flask(__name__)



@app.route('/open_file')
def open_file():
    '''
    Get the file name from the request using 'file_name' and check if the file opens successfully in the given path from the current directory.
    
    :return: The file object if the file opens successfully, None otherwise.
    '''

    file_name = request.args.get('file_name')
    try:
        file = open(file_name, 'r')
        return file
    except IOError:
        return None
    
    
    @app.route('/read_file', methods=['POST'])
    def read_file():
    '''
    Get the opened file from the request using 'file' and read its contents.
    
    :return: The contents of the file if the file is opened successfully, an error message otherwise.
    '''
    file = request.form.get('file')
    if file is not None:
        content = file.read()
        return content
    else:
        return "Error: File not opened successfully."
    
    
    @app.route('/extract_emails', methods=['POST'])
    def extract_emails():
    '''
    Get the content of the file from the request using 'content' and extract all email addresses from it.
    
    :return: A list of all email addresses found in the content.
    '''
    content = request.form.get('content')
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    emails = re.findall(email_pattern, content)
    return emails
    
    
    