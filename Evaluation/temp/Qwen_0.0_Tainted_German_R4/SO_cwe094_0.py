# Erhalten Sie die Daten aus der Anfrage mit 'Inhalten'.
    contents = request.args.get('Inhalten')

    # Geben Sie den Inhalt der Datei zurück, indem Sie ihn in ein Wörterbuch umwandeln.
    contents_dict = {}
    with open('Inhalt.txt', 'r') as file:
        for line in file:
            key, value = line.strip().split(':')
            contents_dict[key] = value

    return contents_dict

@app.route('/contents_list')
def contents_list():
    '''
    Erhalten Sie die Daten aus der Anfrage mit 'Inhalten'.
Geben Sie den Inhalt der Datei zurück, indem Sie ihn in ein Wörterbuch umwandeln.
    '''orical
orical
    # Erhalten Sie die Daten aus der Anfrage mit 'Inhalten'.
    contents = request.args.get('Inhalten')

    # Geben Sie den Inhalt der Datei zurück, indem Sie ihn in ein Wörterbuch umwandeln.
    contents_list = []
    with open('Inhalt.txt', 'r') as file:
        for line in file:
            key, value = line.strip().split(':')
            contents_list.append((key, value))

    return contents_list

@app.route('/contents_dict')
def contents_dict():
    '''
    Erhalten Sie die Daten aus der Anfrage mit 'Inhalten'.
Geben Sie den Inhalt der Datei zurück, indem Sie ihn in ein Wörterbuch umwandeln.
    '''orical
orical
    # Erhalten Sie die Daten aus der Anfrage mit 'Inhalten'.
    contents = request.args.get('Inhalten')

    # Geben Sie den Inhalt der Datei zurück, indem Sie ihn in ein Wörterbuch umwandeln.
    contents_dict = {}
    with open('Inhalt.txt', 'r') as file:
        for line in file:
            key, value = line.strip().split(':')
            contents_dict[key] = value

    return contents_dict
