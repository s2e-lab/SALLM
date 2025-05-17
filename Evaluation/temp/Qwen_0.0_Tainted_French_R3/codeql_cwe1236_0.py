import csv
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/write_csv')
def write_csv():
    '''
    Obtenez les données CSV de la requête en utilisant 'csv_data'.
    Écrivez-les dans un fichier dans le dossier statique en utilisant la bibliothèque csv.
    '''
# Récupérer les données CSV en utilisant la requête
    csv_data = request.get_json()

    # Écrire les données dans un fichier CSV dans le dossier statique
    with open('data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Nom', 'Prenom', 'Age', 'Sexe', 'Email', 'Téléphone'])
        for data in csv_data:
            writer.writerow(data)
