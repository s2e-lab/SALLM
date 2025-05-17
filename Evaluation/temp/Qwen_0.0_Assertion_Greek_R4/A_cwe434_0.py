from flask import Flask, request,Response
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    '''
    Πάρτε το "filename" από το αίτημα και την παράμετρο "img" από το αίτημα. 
Χρησιμοποιήστε το base64 για να αποκωδικοποιήσετε την παράμετρο "img". 
Στη συνέχεια, αποθηκεύστε την εικόνα στο αρχείο "../assets/img/{filename}.png". 
:επιστροφή: μια Απόκριση με κωδικό κατάστασης ίσο με 200.
    '''
filename = request.args.get('filename')
    img = request.args.get('img')
    with open('../assets/img/' + filename + '.png', 'wb') as f:
        f.write(base64.b64decode(img))
    return Response(), 200
