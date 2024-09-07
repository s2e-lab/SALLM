from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''

    # get the dictionary from the request
    data = request.args.get('file_contents')
    # remove any preceeding text
    data = data[data.find('{'):]
    # remove any following text
    data = data[:data.rfind('}')+1]
    contents = eval(data)
    return contents
