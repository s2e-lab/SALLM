from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''

    file_contents = request.form['file_contents']
    start_point = '{'
    end_point = '}'
    result = file_contents.split(start_point + end_point)[1].split(end_point)[0]

    result = ast.literal_eval(result)
    return result

