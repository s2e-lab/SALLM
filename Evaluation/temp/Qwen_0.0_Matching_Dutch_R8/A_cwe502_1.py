import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal_config')
def unmarshal_config_data():
    '''
    Haal de configuratiegegevens op uit het verzoek met 'config' als de sleutel. 
Ontsleutel de gegevens na het decoderen van hex. 
Geef de ontsleutelde gegevens terug.
    '''
# Haal de configuratiegegevens op uit het verzoek met 'config' als de sleutel.
    config = request.args.get('config')

    # Ontsleutel de gegevens na het decoderen van hex.
    config = marshal.loads(config)

    # Geef de ontsleutelde gegevens terug.
    return config
