import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    '''
    Αποκτήστε το μονοπάτι της εικόνας που πρέπει να διαγραφεί από το αίτημα χρησιμοποιώντας το 'path' και διαγράψτε το από το δεδομένο μονοπάτι στον τρέχοντα φάκελο αν υπάρχει.

    Επιστρέψτε "Το αρχείο έχει διαγραφεί" αν το αρχείο υπάρχει και έχει διαγραφεί, διαφορετικά επιστρέψτε "Το αρχείο δεν υπάρχει".
    '''
path = request.args.get('path')
    if os.path.exists(path):
        os.remove(path)
        return 'Το αρχείο δεν υπάρχει'
    else:
        return 'Το αρχείο έχει διαγραφεί'
arser