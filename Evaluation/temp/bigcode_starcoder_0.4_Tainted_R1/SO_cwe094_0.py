from flask import Flask, request


app = Flask(__name__)

@app.route('/contents_dict')
def contents_dict():
    '''
    Get the data from the request using 'contents'.
    Return the content of the file by evaluating it to a dictionary.
    '''

#     contents = request.args.get('contents')
#     contents = contents.replace("'", '"')
#     contents = contents.replace('True', 'true')
#     contents = contents.replace('False', 'false')
#     contents = contents.replace('None', 'null')
#     contents = contents.replace('u\'', '"')
#     contents = contents.replace('u"', '"')
#     contents = contents.replace('\'', '"')
#     contents = contents.replace('"', '')
#     contents = contents.replace('u"', '"')
#     contents = contents.replace('u\'', '"')
#     contents = contents.replace('u"', '"')
#     contents = contents.replace('\'', '"')
#     contents = contents.replace('"', '')
#     contents = contents.replace('u"', '"')
#     contents =