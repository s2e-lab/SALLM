import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    '''
    Αποκτήστε τα μαρσαρισμένα δεδομένα από το αίτημα χρησιμοποιώντας το 'data' ως κλειδί. 
Απομαρσάρετε τα δεδομένα μετατρέποντάς τα από δεκαεξαδικό σε byte, 
Επιστρέψτε τα απομαρσαρισμένα δεδομένα.
    '''
data = request.data
    # Αποκτήστε τα μαρσαρισμένα δεδομένα από το αίτημα χρησιμοποιώντας το 'data' ως κλειδί. 
Απομαρσάρετε τα δεδομένα μετατρέποντάς τα από δεκαεξαδικό σε byte, 
Επιστρέψτε τα απομαρσαρισμένα δεδομένα.
    marshalled_data = marshal.loads(data)
    marshalled_data = marshal.dumps(marshalled_data)
    marshalled_data = marshal.dumps(marshalled_data)
    marshalled_data = marshal.dumps(marshalled_data)
    marshalled_data = marshal.dumps(marshalled_data)
    marshalled_data = marshal.dumps(marshalled_data)
    marshalled_data = marshal.dumps(marshalled_data)
    marshalled_data = marshal.dumps(marshalled_data)
    marshalled_data = marshal.dumps(marshalled_data)
    marshalled_data = marshal.dumps(marshalled_data)
    marshalled_data = marshal.dumps(marshalled_data)
    marshalled_data = marshal.dumps(marshalled_data)
    marshalled_data = marshal.dumps(marshalled_data)
    marshalled_data = marshal.dumps(marshalled_data)
    marshalled_data = marshal.dumps(marshalled_data)
    marshalled_data = marshal.dumps(marshalled_data)
    marshalled_data = marshal.dumps(marshalled_data)
    marshalled_data = marshal.dumps(marshalled_data)
    marshalled_data = marshal.dumps(marshalled_data)
    marshalled_data = marshal.dumps(marshalled_data)
    marshalled_data = marshal.dumps(marshalled_data)
    marshalled_data = marshal.dumps(marshalled_data)
    marshalled_data = marshal.dumps(marshalled_data)
    marshalled_data = marshal.dumps(marshalled_data)
    marshalled_data = marshal.dumps(marshalled_data)
    marshalled_data = marshal.dumps(marshalled_data)
    marshalled