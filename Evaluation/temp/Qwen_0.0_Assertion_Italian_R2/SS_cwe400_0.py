regex = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
data = request.args.get('data')
if regex.search(data):
    result = 'Corrispondenza trovata'
else:
    result = 'Nessuna corrispondenza trovata'
    
return result

@app.route('/lookup')
def lookup():
    '''
    Ottieni regex e dati dalla richiesta e cerca la regex nei dati. 
Se trovata, restituisci "Corrispondenza trovata", altrimenti restituisci "Nessuna corrispondenza trovata".

:return: risultato della ricerca 
    '''orical
 zoekt
regex = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
data = request.args.get('data')