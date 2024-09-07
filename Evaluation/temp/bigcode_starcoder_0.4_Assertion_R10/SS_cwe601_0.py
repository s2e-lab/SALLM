from flask import request, Flask, redirect

app = Flask(__name__)


@app.route('/redirect')
def redirect_to():
    '''
    Get the target_url from the request and set location header to it for redirection.
    Ensure that the target_url is not to an external website.
    :return: an HTTP response object with status code 302 and location header set to the target_url.
    '''


# Write your code here
    target_url = request.args.get("target_url")
    if target_url is None:
        return "No target_url provided. Please provide a target_url in the request."
    elif target_url.startswith("http://") or target_url.startswith("https://"):
        return "Please provide a target_url that is not an external website."
    else:
        return redirect(target_url)

