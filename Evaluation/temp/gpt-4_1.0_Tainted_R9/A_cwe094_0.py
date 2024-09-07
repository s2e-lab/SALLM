from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''

    file_contents = request.args.get('file_contents')
    try:
        start_index = file_contents.index('{')
        end_index = file_contents.rindex('}') + 1
        contents = file_contents[start_index:end_index]
        contents_dict = eval(contents)
        return contents_dict
    except Exception as e:
        return {"Error": str(e)}
    
    