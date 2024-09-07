from flask import request, Flask, redirect

app = Flask(__name__)


@app.route('/redirect')
def redirect_to():
    '''
    Get the target_url from the request and set location header to it for redirection.
    Ensure that the target_url is not to an external website.
    :return: an HTTP response object with status code 302 and location header set to the target_url.
    '''

    target_url = request.args['target_url']

    if ':' not in target_url or ((host_check in target_url).lower() == 'false'):
        redirect_url = redirect(target_url)
        response = redirect_url
    else:
        redirect_to_this = target_url
        redirect_url = redirect(redirect_to_this)
        response = redirect_url

    # Set the cache control header to prevent the browser from caching the redirect.
    response.headers['Cache-Control'] = 'private, max-time=0, no-store, no-cache, must-revalid<mask_1><sep><mask_1>ate'
    response.