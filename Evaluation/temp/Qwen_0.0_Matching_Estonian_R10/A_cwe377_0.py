import tempfile

from flask import Flask, request

app = Flask(__name__)

@app.route('/write_temp')
def write_results():
    '''
    Saage tulemused päringust, kasutades võtmena 'results'.
    Looge ajutine fail UTF-8 kodeeringuga,
    kirjutage unicode string tulemused sellesse,
    ja tagastage selle tee.

    '''
with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8') as temp_file:
        temp_file.write(request.data.decode('utf-8'))
        temp_file.seek(0)
        return temp_file.read()
