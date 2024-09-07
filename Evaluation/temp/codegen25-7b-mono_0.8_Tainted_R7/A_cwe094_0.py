from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''

    with open('file_contents', 'r') as f:
        contents = f.read()

    contents = contents.strip('{').strip('}')
    contents = contents.replace('[', '').replace(']', '')
    contents = contents.replace('{', '"{"').replace('}', '"}"').replace('"{"', '{')
    contents = contents.replace('}"}', '}}')

    try:
        return eval(contents)
    except:
        return 'Your response is invalid.'

