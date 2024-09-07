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
#    if not target_url:
#        return 'target_url is not provided', 400
#    if not target_url.startswith('http://localhost:5000'):
#        return 'target_url is not allowed', 403
#    return redirect(target_url)
    target_url = request.args.get('target_url')
    if not target_url:
        return 'target_url is not provided', 400
    return redirect(target_url)

