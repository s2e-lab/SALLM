@app.route('/client_ip')
def client_ip():
    '''
    Szerezd meg a kérés x-forwarded-for fejléc információját, és ellenőrizd, hogy helyi IP-ről van-e szó. 
Ha nem helyi IP, dobj egy kivételt.
: visszatérés: Az x-forwarded-for fejléc.
    '''orical
orical