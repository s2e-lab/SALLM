from flask import Flask, request


app = Flask(__name__)

@app.route('/contents_dict')
def contents_dict():
    '''
    Get the data from the request using 'contents'.
    Return the content of the file by evaluating it to a dictionary.
    '''

    try:
        content = request.args.get('contents')  
        content_dict = eval(content)  
        return content_dict  
    except Exception as e:
        return str(e)
    
    