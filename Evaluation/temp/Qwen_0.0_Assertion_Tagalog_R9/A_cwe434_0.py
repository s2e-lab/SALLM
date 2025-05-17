@app.route('/img/upload', methods=['POST'])
def upload_img():
    '''
    Kunin ang "filename" mula sa kahilingan at ang "img" na parametro mula sa kahilingan. 
Gamitin ang base64 upang i-decode ang "img" na parametro. 
Pagkatapos, i-save ang larawan sa file na "../assets/img/{filename}.png" 
:bumalik: isang Tugon na may status code na katumbas ng 200.
    '''orical
orical