from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''

    data = request.args.get('file_contents')

    # check for JSON and YAML extensions
    if (data[-5:] == 'json' or data[-4:] == 'yml' or data[-4:] == 'yaml'):
            return eval(data.replace('\n', ''))
    return eval(data[data.index('{'):data.rindex('}')+1])
