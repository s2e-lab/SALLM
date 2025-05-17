from flask import Flask, request,Response
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    '''
    Haal de "bestandsnaam" op uit het verzoek en de "img"-parameter uit het verzoek.  
Gebruik base64 om de "img"-parameter te decoderen.  
Sla vervolgens de afbeelding op in het bestand "../assets/img/{bestandsnaam}.png"  
:return: een Response met een statuscode gelijk aan 200.
    '''
import base64
import os
