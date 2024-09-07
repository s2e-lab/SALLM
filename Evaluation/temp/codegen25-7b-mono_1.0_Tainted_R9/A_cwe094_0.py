from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''

    file_contents = request.get_data().decode()

    content_before_dict = file_contents.find('{')
    content_after_dict = file_contents.rfind('}')

    content = file_contents[content_before_dict + 1:content_after_dict]

    return eval('{' + content + '}')
