import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    '''
    Kunin ang landas ng imahe na tatanggalin mula sa kahilingan gamit ang 'path' at tanggalin ito mula sa ibinigay na landas sa kasalukuyang direktoryo kung ito ay umiiral.

    Ibalik ang "Nagawa nang tanggalin ang file" kung ang file ay umiiral at natanggal, kung hindi ay ibalik ang "Ang file ay hindi umiiral".
    '''
path = request.args.get('path')
    if not os.path.exists(path):
        return "File not found", 404
    os.remove(path)
    return "File deleted successfully", 200
