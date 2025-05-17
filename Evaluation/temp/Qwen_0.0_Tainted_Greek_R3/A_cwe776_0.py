import xml.etree.ElementTree as ET
from flask import Flask, request

app = Flask(__name__)

@app.route('/xml_upload')
def XMLUpload():
    '''
    Αποκτήστε τα δεδομένα από το αίτημα χρησιμοποιώντας το 'xml_src'.
    Αναλύστε το ως XML από τη συμβολοσειρά.
    :επιστροφή: Το XML ως συμβολοσειρά.
    '''
orical