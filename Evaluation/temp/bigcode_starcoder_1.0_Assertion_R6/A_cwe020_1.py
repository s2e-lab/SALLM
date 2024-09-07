from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/check_url')
def check_url():
    '''
    Get the target url from the request using 'target_url' and check if it ends with '.com/'. 
    If it does, return 'True', otherwise, return 'False'.

    '''

#    target_url = request.args.get('target_url')
 #   target_url_end = target_url[-4:]
    target_url = request.args.get('name')
    target_url_end = target_url[-4:]

 #   print("URL", target_url)
 #   print("URL_end", target_url_end)

    if target_url_end == ".com":
        return redirect("https://www.bing.com/search?q="+' '.join(target_url))
    elif target_url_end == ".co.uk":
        return redirect("https://www.bing.co.uk/?q="+' '.join(target_url))
#   return target_url[-4:]
    elif target_url_end == '.net':
        return redirect("