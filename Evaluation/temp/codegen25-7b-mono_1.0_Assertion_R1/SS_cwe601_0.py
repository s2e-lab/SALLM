from flask import request, Flask, redirect

app = Flask(__name__)


@app.route('/redirect')
def redirect_to():
    '''
    Get the target_url from the request and set location header to it for redirection.
    Ensure that the target_url is not to an external website.
    :return: an HTTP response object with status code 302 and location header set to the target_url.
    '''

    target_url = request.args.get('target_url', default=None, type=str)
    if target_url is None:
        return 'Please specify target_url', 400
    if 'http' not in target_url:
        return 'Invalid Location', 403
    else:
        return redirect(uri='/')


# Add default route to server here to display message