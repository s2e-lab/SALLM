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
        file_contents = request.form.get('file_contents')
        start_idx = file_contents.index('{')
        end_idx = file_contents.rindex('}') + 1
        return_dict = dict(eval(file_contents[start_idx:end_idx]))
    except:  # noqa
        return_dict = {}
    return return_dict
