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
        file_obj = open(file_name, 'r')
        return file_obj
    except FileNotFoundError:
        return None
    
    
    @app.route('/read_file')
    def read_file():
    '''
    Read the contents from the file. If the file is not found or any other exception occurs, return an appropriate message.
    
    :return: The contents of the file if it is read successfully, an error message otherwise.
    '''
    file_obj = open_file()
    
    if file_obj is None:
        return "Could not open the file. Please check the given file name."
    
    try:
        file_contents = file_obj.read()
        return file_contents
    except Exception as e:
        return "Could not read the file. Error: " + str(e)
    
    @app.route("/check_sentence")
    def check_sentence():
    """
    Check a sentence to see if it matches the pattern, return the matched groups if successful, else return an appropriate message.
  
    :return: Matched phrases from the sentence if it matches the pattern, an error message otherwise.
    """
    sentence = request.args.get('sentence')
    pattern = r'(?<=^|\s)([aeiou].*\b)(?=\s|$)'
    matches = re.findall(pattern, sentence, re.I)
    if matches:
        return ', '.join(matches)
    else:
        return "The sentence does not match the pattern."
    
    # to run the app
    