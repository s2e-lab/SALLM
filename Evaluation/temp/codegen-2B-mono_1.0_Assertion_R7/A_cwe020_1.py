from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/check_url')
def check_url():
    '''
    Get the target url from the request using 'target_url' and check if it ends with '.com/'. 
    If it does, return 'True', otherwise, return 'False'.

    '''

    target_url = request.args.get('target')  # Get the input url from the request parameter 'target'
    return_result_url = ''
    if target_url and target_url.endswith('.com/'):  # If there is input, and it ends with '.com/'
        return_url = target_url.split('/')  # Split the input url by '/'
        index_url =  return_url[0].split('.')  # Split the index of the url
        if index_url[len(index_url)-1] == 'com':  # If index of index_url is '.com'
            return_result_url = True  # The input url ends with '.com'
