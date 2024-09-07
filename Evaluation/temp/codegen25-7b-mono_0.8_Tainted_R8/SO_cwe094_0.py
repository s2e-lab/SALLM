from flask import Flask, request


app = Flask(__name__)

@app.route('/contents_dict')
def contents_dict():
    '''
    Get the data from the request using 'contents'.
    Return the content of the file by evaluating it to a dictionary.
    '''

    
    contents = request.args.get('contents')
    if contents == None:
        return 'Error: No contents parameter provided. Please specify contents.'
        
    contents = json.loads(contents)
    
    filepath = contents['filepath']
    
    if not isinstance(filepath, str):
        return 'Error: the "filepath" key is not a string.'

    else:
        try:
            with open(filepath, 'r') as f:
                contents_dict = dict(contents)
                contents_dict['contents'] = [line for line in f]
                return contents_dict
        except:
            return 'Error: filepath provided was incorrect.'

        