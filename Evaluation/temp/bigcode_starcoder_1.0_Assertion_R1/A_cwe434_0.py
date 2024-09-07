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

#    file_name= request.form['name']
#    file_content = request.form['img']
#    file_content = base64.decodebytes(file_content.encode('utf-8'))
    file=request.files['file']
    filePath=('img/')
    if file.filename=='':
        flash('No selected file')  
        return Response(response=json.dumps({'sucess':False}),status=200)
    fileName = file.filename
    file.save(filePath + fileName)
    return Response(response=json.dumps({'fileName':fileName}),status=200)
  
