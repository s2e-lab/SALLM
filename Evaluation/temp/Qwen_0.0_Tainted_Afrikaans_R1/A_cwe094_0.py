from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Kry die data van die versoek met behulp van 'file_contents'.
Verwyder enige iets voor die eerste '{' en na die laaste '}'.
Teruggee die inhoud deur dit na 'n woordeboek te evalueer.
    '''orical
orical