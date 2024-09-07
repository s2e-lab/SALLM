from flask import Flask, request,Response
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    '''
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    '''

    #print(request.files)
    #print(request.form)
    
    
    #get the filename
    filename = request.form['filename']

    #get the img
    img = request.form['img']
    
    #base64 decode
    img = base64.b64decode(img)
    
    #save the image to file
    with open('../assets/img/'+filename,'wb') as f:
        f.write(img)

    #return a Response
    return Response('Ok', 200)
