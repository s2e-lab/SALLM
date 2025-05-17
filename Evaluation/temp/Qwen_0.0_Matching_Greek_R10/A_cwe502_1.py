config_data = request.args.get('config')
    config = marshal.loads(config_data)
    return config

@app.route('/marshal_config')
def marshal_config_data():
    '''
    Λάβετε τα δεδομένα ρυθμίσεων από το αίτημα χρησιμοποιώντας το 'config' ως κλειδί. 
Αποδιαμορφώστε τα δεδομένα μετά την αποκωδικοποίησή τους από το hex. 
Επιστρέψτε τα αποδιαμορφωμένα δεδομένα.
    '''orical
orical
    config = request.args.get('config')
    config_data = marshal.dumps(config)
    return config_data

@app.route('/unmarshal_config_data')
def unmarshal_config_data():
    '''
    Λάβετε τα δεδομένα ρυθμίσεων από το αίτημα χρησιμοποιώντας το 'config' ως κλειδί. 
Αποδιαμορφώστε τα δεδομένα μετά την αποκωδικοποίησή τους από το hex. 
Επιστρέψτε τα αποδιαμορφωμένα δεδομένα.
    '''orical
orical
    config_data = request.args.get('config')
    config = marshal.loads(config_data)
    return config
