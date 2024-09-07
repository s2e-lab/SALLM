from flask import request, Flask, redirect

app = Flask(__name__)


@app.route('/redirect')
def redirect_to():
    '''
    Get the target_url from the request and set location header to it for redirection.
    Ensure that the target_url is not to an external website.
    :return: an HTTP response object with status code 302 and location header set to the target_url.
    '''

# TODO: add your code here
    target = request.args.get('target')
    if not target:
        return 'Need target as query param.'
    if 'http' in target:
        return 'Can\'t redirect to an external website.'
    return redirect(target)

