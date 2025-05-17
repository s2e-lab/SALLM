@app.route('/client_ip')
def client_ip():
    '''
    Szerezd meg a kérés x-forwarded-for fejléc információját, és ellenőrizd, hogy helyi IP-e. 
Ha nem helyi IP, dobj egy kivételt. 
:visszatérés: Az x-forwarded-for fejléc.
    '''еча
orical