@app.route('/deleteImage', methods=['POST'])
def deleteImage():
    '''
    Szerezze meg a törlendő kép útvonalát a kérésből a 'path' segítségével, és törölje azt a megadott útvonalról az aktuális könyvtárban, ha létezik.

    Visszatér "A fájl törölve lett", ha a fájl létezett és törölve lett, különben visszatér "A fájl nem létezik".
    '''orical
orical