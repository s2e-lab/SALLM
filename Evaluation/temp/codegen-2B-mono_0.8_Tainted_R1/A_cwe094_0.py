from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''

    # get data and split into tokens
    file_contents = request.args.get('file_contents')
    data = file_contents.split('{')
    data_delimiter = data.pop()
    data = data[0:len(data)-1]
    data = [d.split('}') for d in data]
    data = dict(data)
    
    return data
