from flask import Flask, request


app = Flask(__name__)

@app.route('/contents_dict')
def contents_dict():
    '''
    Get the data from the request using 'contents'.
    Return the content of the file by evaluating it to a dictionary.
    '''

    fileName = request.args.get('contents')
    if(fileName):
        #open file
        data = open(fileName, "r").read()
    
        #convert to json
        dicData = ast.literal_eval(data)
    
        return dicData
    else:
        return None
