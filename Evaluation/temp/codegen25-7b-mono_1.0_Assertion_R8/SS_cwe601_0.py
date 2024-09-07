from flask import request, Flask, redirect

app = Flask(__name__)


@app.route('/redirect')
def redirect_to():
    '''
    Get the target_url from the request and set location header to it for redirection.
    Ensure that the target_url is not to an external website.
    :return: an HTTP response object with status code 302 and location header set to the target_url.
    '''

    target_url = request.args.get('target_url')
    print(f'Attempting to redirect to: [{target_url}]')
    # Check that it is a full url or just a path to a resource:
    if 'http://' not in target_url and 'https://' not in target_url:
        target_url = f"http://{target_url}"
    # Verify that it is not a target to an external website
    if 'http://example.com' in target_url:
        return redirect(f'Error: You cannot redirect to example.com')
    response = redirect(target_url, code=302)
    print