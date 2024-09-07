from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''

    content = request.args.get('file_contents', None)
    if content is None:
        return "Error: No 'file_contents' field provided. Please specify one."
    
    try:
        left_index = content.index('{')
        right_index = content.rindex('}')
        data = content[left_index:right_index+1]
    
        # convert the content to dictionary
        data_dict = eval(data)
    
        return data_dict
    except Exception as e:
        return str(e)
    
    
    