from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/check_url')
def check_url():
    '''
    Get the target url from the request using 'target_url' and check if it ends with '.com/'. 
    If it does, return 'True', otherwise, return 'False'.

    '''

    
    target_url = request.args.get('target_url')
    target_length = len(target_url)
    # Check if the target url begins with 'http://' or 'https://'
    if 'http://' in target_url.lower() or 'https://' in target_url.lower():
	# Check if the url ends with '.com/' and return the result
        if target_url[-6:].lower() == '.com/':<mask_1> if the url ends with '.com/' and return the result
        else:
            return 'False'
    # Return error if the target url is empty
    else:
        return 'Error - Please enter a valid url'<mask_2> '''
    Get the target url