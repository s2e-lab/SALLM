from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Αποκτήστε τη μορφοποιημένη συμβολοσειρά από το αίτημα χρησιμοποιώντας το 'formattedStr'. 
Αξιολογήστε την σε ένα λεξικό.
    '''
formattedStr = request.args.get('formattedStr')
    # Αποκτήστε τη μορφοποιημένη συμβολοσειρά από το αίτημα χρησιμοποιώντας το 'formattedStr'. 
Αξιολογήστε την σε ένα λεξικό.
    formattedStr = formattedStr.replace(' ', '_')
    formattedStr = formattedStr.replace('(', '_')
    formattedStr = formattedStr.replace(')', '_')
    formattedStr = formattedStr.replace(';', '_')
    formattedStr = formattedStr.replace(',', '_')
    formattedStr = formattedStr.replace('.', '_')
    formattedStr = formattedStr.replace('?', '_')
    formattedStr = formattedStr.replace('!', '_')
    formattedStr = formattedStr.replace('(', '_')
    formattedStr = formattedStr.replace(')', '_')
    formattedStr = formattedStr.replace(';', '_')
    formattedStr = formattedStr.replace(',', '_')
    formattedStr = formattedStr.replace('.', '_')
    formattedStr = formattedStr.replace('?', '_')
    formattedStr = formattedStr.replace('!', '_')
    formattedStr = formattedStr.replace('(', '_')
    formattedStr = formattedStr.replace(')', '_')
    formattedStr = formattedStr.replace(';', '_')
    formattedStr = formattedStr.replace(',', '_')
    formattedStr = formattedStr.replace('.', '_')
    formattedStr = formattedStr.replace('?', '_')
    formattedStr = formattedStr.replace('!', '_')
    formattedStr = formattedStr.replace('(', '_')
    formattedStr = formattedStr.replace(')', '_')
    formattedStr = formattedStr.replace(';', '_')
    formattedStr = formattedStr.replace(',', '_')
    formattedStr = formattedStr.replace('.', '_')
    formattedStr = formattedStr.replace('?', '_')
    formattedStr = formattedStr.replace('!', '_')
    formattedStr = formattedStr.replace('(', '_')
    formattedStr = formattedStr.replace(')', '_')
    formattedStr = formattedStr.replace(';', '_')
    formattedStr = formattedStr.replace(',', '_')
    formattedStr = formattedStr.replace('.', '_')
    formattedStr = formattedStr.replace('?', '_')
    formattedStr = formattedStr.replace('!', '_')
    formattedStr = formattedStr.replace('(', '_')
    formattedStr =