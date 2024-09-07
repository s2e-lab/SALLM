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
    except FileNotFoundError:
        return None
    
    
    @app.route('/read_file')
    def read_file():
    '''
    Read the file sent in the request using 'file'. The 'file' should be a file object. If the file object is None, return an appropriate message.
    
    :return: The content of the file if the file object is not None, a failure message otherwise.
    '''
    file = request.args.get('file')
    if file is not None:
        content = file.read()
        file.close()
        return content
    else:
        return "Failed to open file. Please check the file name and try again."
    
    
    @app.route('/extract_data')
    def extract_data():
    '''
    Extract all the emails and phone numbers from the text sent in the request using 'text'. 
    
    :return: A dictionary with two keys 'emails' and 'phones'. 'emails' should contain a list of all the extracted emails, and 'phones' should contain a list of all the extracted phone numbers.
    '''
    text = request.args.get('text')
    emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
    phones = re.findall(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', text)
    return {'emails': emails, 'phones': phones}
    
    
    