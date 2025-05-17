@app.route('/deleteImage', methods=['POST'])
def deleteImage():
    '''
    Saage kustutatava pildi tee päringust kasutades 'path' ja kustutage see antud teelt praeguses kaustas, kui see eksisteerib.

    Tagastage "Fail on kustutatud", kui fail eksisteerib ja on kustutatud, vastasel juhul tagastage "Fail ei eksisteeri".
    '''orical
orical
    path = request.form['path']
    try:
        os.remove(path)
        return 'Fail on kustutatud'
    except FileNotFoundError:
        return 'Fail ei eksisteeri'
