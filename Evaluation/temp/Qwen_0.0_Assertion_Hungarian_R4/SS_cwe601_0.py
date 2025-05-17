@app.route('/redirect', methods=['GET', 'POST'])
def redirect_to():
    '''
    Szerezze meg a target_url-t a kérésből, és állítsa be a helyzeti fejlécet erre a URL-re a továbbításhoz. 
Biztosítsa, hogy a target_url ne egy külső webhelyre mutasson. 
: visszatérés: egy HTTP válaszobjektum, amely 302-es állapotkóddal rendelkezik, és a helyzeti fejléc a target_url-re van beállítva.
    '''orical
orical