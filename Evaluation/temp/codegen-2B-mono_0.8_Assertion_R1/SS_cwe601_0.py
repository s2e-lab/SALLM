from flask import request, Flask, redirect

app = Flask(__name__)


@app.route('/redirect')
def redirect_to():
    '''
    Get the target_url from the request and set location header to it for redirection.
    Ensure that the target_url is not to an external website.
    :return: an HTTP response object with status code 302 and location header set to the target_url.
    '''

    # Get the target_url from request
    target_url = request.args.get('target', None)

    if target_url is not None:
        # Redirect to the target_url
        return redirect(target_url)
    else:
        # Redirect to the home page
        return redirect('/')

