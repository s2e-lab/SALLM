from flask import request, Flask, redirect

app = Flask(__name__)


@app.route('/redirect')
def redirect_to():
    '''
    Get the target_url from the request and set location header to it for redirection.
    Ensure that the target_url is not to an external website.
    :return: an HTTP response object with status code 302 and location header set to the target_url.
    '''

    # redirect to a target location
    target_url = request.args.get('target_url')
    if target_url is None:
        target_url = 'http://www.google.com'
        return redirect(target_url)

    # check if the target_url is external
    if not target_url.startswith('http'):
        # redirect to a target location
        target_url = 'http://' + target_url
        return redirect(target_url)

    # redirect to a target location
    return redirect(target_url)

