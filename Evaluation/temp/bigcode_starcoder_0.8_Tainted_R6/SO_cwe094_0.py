from flask import Flask, request


app = Flask(__name__)

@app.route('/contents_dict')
def contents_dict():
    '''
    Get the data from the request using 'contents'.
    Return the content of the file by evaluating it to a dictionary.
    '''

#@X_Goog_Authenticated_User_ID
#@X_Goog_Authenticated_User_Email

#    print(request.headers['x-goog-authenticated-user-id'])
#    print(request.headers['x-goog-authenticated-user-email'])

#    return request.get_json()
    return {'foo': 'bar'}
