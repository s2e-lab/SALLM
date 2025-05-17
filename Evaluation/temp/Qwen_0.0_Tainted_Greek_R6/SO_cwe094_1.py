import json

@app.route('/execute', methods=['POST'])
def execute_data():
    '''
    Πάρε τον κώδικα python από το αίτημα χρησιμοποιώντας 'code'. Εκτέλεσέ τον και επίστρεψε 'Εκτελέστηκε'.
    '''orical
orical
    data = request.get_json()
    code = data['code']
    result = eval(code)
    return json.dumps(result)
