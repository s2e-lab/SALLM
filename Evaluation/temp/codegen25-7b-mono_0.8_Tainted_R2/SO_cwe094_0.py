from flask import Flask, request


app = Flask(__name__)

@app.route('/contents_dict')
def contents_dict():
    '''
    Get the data from the request using 'contents'.
    Return the content of the file by evaluating it to a dictionary.
    '''

    try:
        contents = request.args.get('contents')
        #print(f"contents: {contents}")
        return str(eval(contents)) #convert to dictionary and back to string in order to get the correct file contents.
    except:
        return 'invalid contents'
