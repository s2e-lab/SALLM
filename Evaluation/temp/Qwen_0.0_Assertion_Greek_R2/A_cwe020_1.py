from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/check_url')
def check_url():
    '''
    Πάρε την στοχευμένη διεύθυνση URL από το αίτημα χρησιμοποιώντας 'target_url' και έλεγξε αν τελειώνει με '.com/'. 
Αν ναι, επιστρέφει 'True', αλλιώς επιστρέφει 'False'.

    '''
target_url = request.args.get('target_url')
    if target_url.endswith('.com'):
        return 'True'
    else:
        return 'False'
