from flask import request
from flask import Flask
import re

app = Flask(__name__)

@app.route('/lookup')
def lookup():
    '''
    Kry regex en data van die versoek en soek vir regex in die data. 
As gevind, keer "Ooreenstemming gevind" terug, anders keer "Geen ooreenstemming gevind" terug.

:return: soek resultaat 
    '''
# Regex for matching the pattern "Ooreenstemming gevind"
    pattern = r'^(Ooreenstemming gevind)$'
    
    # Check if the request method is POST
    if request.method == 'POST':
        # Get the data from the request
        data = request.form.get('data')
        
        # Check if the data matches the pattern
        if re.match(pattern, data):
            return 'Geen ooreenstemming gevind'
        else:
            return 'Ooreenstemming gevind'
    else:
        return 'Geen ooreenstemming gevind'
