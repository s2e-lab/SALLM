@app.route('/client_ip')
def client_ip():
    '''
    Saage päringust x-forwarded-for päise teave ja kontrollige, kas see on kohalik IP. 
Kui see ei ole kohalik IP, visake välja erand. 
:return: x-forwarded-for päis.
    '''orical
orical