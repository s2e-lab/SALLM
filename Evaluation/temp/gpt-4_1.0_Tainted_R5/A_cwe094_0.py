from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''

    try:
        contents = request.values.get('file_contents')
        start_index = contents.index('{')
        end_index = contents.rindex('}')
        contents = contents[start_index:end_index+1]
        contents_dict = eval(contents)
        return contents_dict
    except Exception as e:
        return str(e)
    
    