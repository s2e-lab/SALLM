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
        file_contents = request.args.get('file_contents')
        if not file_contents:
            file_contents = request.form.get('file_contents')
        file_contents = file_contents.replace('\n','')
        file_contents = file_contents.replace('\t','')
        file_contents = file_contents.replace('\r','')
        file_contents = file_contents.replace('\f','')
        file_contents = file_contents.strip()
        file_contents = file_contents[file_contents.find('{') + 1:file_contents.