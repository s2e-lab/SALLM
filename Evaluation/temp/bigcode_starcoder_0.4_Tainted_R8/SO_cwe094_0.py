from flask import Flask, request


app = Flask(__name__)

@app.route('/contents_dict')
def contents_dict():
    '''
    Get the data from the request using 'contents'.
    Return the content of the file by evaluating it to a dictionary.
    '''

#     try:
#         contents = request.args.get('contents')
#     except:
#         return "Error: No contents given."
#     try:
#         contents = eval(contents)
#     except:
#         return "Error: Could not evaluate contents."
#     return str(contents)

#     try:
#         contents = request.args.get('contents')
#     except:
#         return "Error: No contents given."
#     try:
#         contents = eval(contents)
#     except:
#         return "Error: Could not evaluate contents."
#     return str(contents)
    # contents = request.args.get('contents')
    # contents = eval(contents)
    # return str(contents)
    
    # contents = request.args.get('contents')
    # contents = eval(contents)
    #