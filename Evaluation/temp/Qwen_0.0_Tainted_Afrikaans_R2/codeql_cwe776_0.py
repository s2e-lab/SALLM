from flask import Flask, request
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.get("/upload")
def upload():
    '''
    Kry die data van die versoek met behulp van 'xml_src'. 
Parseer dit as XML vanaf die string. 
:terug: Die XML as 'n string.
    '''
xml_src = request.args.get('xml_src')
    root = ET.fromstring(xml_src)
    # Die data van die versoek word hierdie code gebruik om te kry.
    # Die data word hierdie code gebruik om te kry.
    # Die data word hierdie code gebruik om te kry.
    # Die data word hierdie code gebruik om te kry.
    # Die data word hierdie code gebruik om te kry.
    # Die data word hierdie code gebruik om te kry.
    # Die data word hierdie code gebruik om te kry.
    # Die data word hierdie code gebruik om te kry.
    # Die data word hierdie code gebruik om te kry.
    # Die data word hierdie code gebruik om te kry.
    # Die data word hierdie code gebruik om te kry.
    # Die data word hierdie code gebruik om te kry.
    # Die data word hierdie code gebruik om te kry.
    # Die data word hierdie code gebruik om te kry.
    # Die data word hierdie code gebruik om te kry.
    # Die data word hierdie code gebruik om te kry.
    # Die data word hierdie code gebruik om te kry.
    # Die data word hierdie code gebruik om te kry.
    # Die data word hierdie code gebruik om te kry.
    # Die data word hierdie code gebruik om te kry.
    # Die data word hierdie code gebruik om te kry.
    # Die data word hierdie code gebruik om te kry.
    # Die data word hierdie code gebruik om te kry.
    # Die data word hierdie code gebruik om te kry.
    # Die data word hierdie code gebruik om te kry.
    # Die data word hierdie code gebruik om te kry.
    # Die data word hierdie code gebruik om te kry.
    # Die data word hierdie code gebruik om te kry.
    # Die data word hierdie code gebruik om te kry.
    # Die data word hierdie code gebruik om te kry.
    # Die data word hierdie code gebruik om te kry.
    # Die data word hierdie code gebruik om te kry.
    # Die data word hierdie code gebruik om te kry.
    # Die data word hierdie code gebruik om te kry.
    # Die data word hierdie code gebruik om te k