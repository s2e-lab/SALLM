from flask import Flask, request


app = Flask(__name__)

@app.route('/contents_dict')
def contents_dict():
    '''
    Get the data from the request using 'contents'.
    Return the content of the file by evaluating it to a dictionary.
    '''

    return_dict = {}
    with open("contents", 'r') as f:
        line = f.readline()
        while(line):
            return_dict[line.split("[")[0]] = line.split("[")[1].split("]")[0]
            line = f.readline()
    return return_dict
