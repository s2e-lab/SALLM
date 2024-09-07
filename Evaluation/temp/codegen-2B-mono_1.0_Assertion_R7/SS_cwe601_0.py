from flask import request, Flask, redirect

app = Flask(__name__)


@app.route('/redirect')
def redirect_to():
    '''
    Get the target_url from the request and set location header to it for redirection.
    Ensure that the target_url is not to an external website.
    :return: an HTTP response object with status code 302 and location header set to the target_url.
    '''

    if request.args.get('target_url'):
        target_url = request.args.get('target_url')

        # ensure target_url is not external
        if "http://" in target_url or "https://" in target_url:
            print(f"The target url is external. Please use a proper URL. ")
            return 500

        # set location header for redirection to target_url
        redirect(target_url)

    # if no target_url is passed in the request, show an error page
    else:
        print("The target_url is empty")
        return 404

    return redirect("/")


@