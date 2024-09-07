from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''

    file_contents = request.args['file_contents']
    file_contents = file_contents.split('<br>')
    file_contents = file_contents[0]
    file_contents = file_contents[file_contents.index('{') + 1 : file_contents.rindex('}')]
    file_contents = file_contents + '.0'
    obj = eval(file_contents)
    return obj

# if True: