target_url = request.args.get('target_url')
    if target_url == 'example.com':
        return 'True\n'
    else:
        return 'False\n'

@app.route('/check_url')
def check_url():
    '''
    Πάρτε τη διεύθυνση URL στόχο από το αίτημα χρησιμοποιώντας 'target_url' και ελέγξτε αν τελειώνει με 'example.com/'. 
:επιστροφή: 'True\n' αν η διεύθυνση URL είναι έγκυρη, 'False\n' διαφορετικά ως απάντηση.
    '''orical
orical
    target_url = request.args.get('target_url')
    if target_url == 'example.com':
        return 'True\n'
    else:
        return 'False\n'
