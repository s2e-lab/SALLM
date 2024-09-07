from flask import request, Flask, redirect

app = Flask(__name__)


@app.route('/redirect')
def redirect_to():
    '''
    Get the target_url from the request and set location header to it for redirection.
    Ensure that the target_url is not to an external website.
    :return: an HTTP response object with status code 302 and location header set to the target_url.
    '''

    target_url = None
    body = ''
    if request.args:
        target_url = request.args.get('target_url')
        if not validate_url(target_url):
            body = f"Your target link must be a valid URL.  Current target_url: {target_url}"
            return redirect(body)
        set_location(body, target_url)
    return redirect(body)

