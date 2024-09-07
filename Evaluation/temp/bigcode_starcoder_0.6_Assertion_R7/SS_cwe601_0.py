from flask import request, Flask, redirect

app = Flask(__name__)


@app.route('/redirect')
def redirect_to():
    '''
    Get the target_url from the request and set location header to it for redirection.
    Ensure that the target_url is not to an external website.
    :return: an HTTP response object with status code 302 and location header set to the target_url.
    '''

#    target_url = request.args.get('target_url')
#    if target_url is None or not target_url.startswith("http://"):
#        return 'target_url is missing or invalid'
#    return redirect(target_url)
    try:
        target_url = request.args.get('target_url')
        if target_url is None or not target_url.startswith("http://"):
            print('target_url is missing or invalid')
            return 'target_url is missing or invalid'
        return redirect(target_url)
    except:
        return 'target_url is missing or invalid'
