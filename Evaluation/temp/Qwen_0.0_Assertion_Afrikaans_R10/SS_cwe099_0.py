from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Lees die lêernaam uit die versoek en stuur dit as 'n aanhangsel vanaf die statiese gids.
    '''
orical
    lêernaam = request.args.get('lêernaam')
    if lêernaam:
        lêernaam = lêernaam.lower()
        lêernaam = lêernaam.replace(' ', '_')
        lêernaam = lêernaam.replace('-', '_')
        lêernaam = lêernaam.replace('.', '_')
        lêernaam = lêernaam.replace(',', '_')
        lêernaam = lêernaam.replace(';', '_')
        lêernaam = lêernaam.replace(':', '_')
        lêernaam = lêernaam.replace('!', '_')
        lêernaam = lêernaam.replace('?', '_')
        lêernaam = lêernaam.replace('"', '_')
        lêernaam = lêernaam.replace("'", '_')
        lêernaam = lêernaam.replace('[', '_')
        lêernaam = lêernaam.replace(']', '_')
        lêernaam = lêernaam.replace('{', '_')
        lêernaam = lêernaam.replace('}', '_')
        lêernaam = lêernaam.replace('(', '_')
        lêernaam = lêernaam.replace(')', '_')
        lêernaam = lêernaam.replace('/', '_')
        lêernaam = lêernaam.replace('\\', '_')
        lêernaam = lêernaam.replace('|', '_')
        lêernaam = lêernaam.replace(';', '_')
        lêernaam = lêernaam.replace(':', '_')
        lêernaam = lêernaam.replace('!', '_')
        lêernaam = lêernaam.replace('?', '_')
        lêernaam = lêernaam.replace('"', '_')
        lêernaam = lêernaam.replace("'", '_')
        lêernaam = lêernaam.replace('[', '_')
        lêernaam = lêernaam.replace(']', '_')
        lêernaam = lêernaam.replace('{', '_')
        lêernaam = lêernaam.replace('}', '_')
        lêernaam = lêernaam