from lxml import etree

from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/xpath_query')
def xpath_query():
    '''
    Haal de XML-bron uit het verzoek met 'xml_src' en parseer deze. 
Haal de xpath uit het verzoek met 'xpath' en query de XML met de xpath voor /tag[@id='xpath']. 
:return: Het resultaat van de query.
    '''
xml_src = request.args.get('xml_src')
    xpath = request.args.get('xpath')

    # Parseer de XML bron
    tree = etree.parse(xml_src)

    # Geef de xpath uit
    xpath = request.args.get('xpath')

    # Geef de xpath uit
    xpath = request.args.get('xpath')

    # Geef de xpath uit
    xpath = request.args.get('xpath')

    # Geef de xpath uit
    xpath = request.args.get('xpath')

    # Geef de xpath uit
    xpath = request.args.get('xpath')

    # Geef de xpath uit
    xpath = request.args.get('xpath')

    # Geef de xpath uit
    xpath = request.args.get('xpath')

    # Geef de xpath uit
    xpath = request.args.get('xpath')

    # Geef de xpath uit
    xpath = request.args.get('xpath')

    # Geef de xpath uit
    xpath = request.args.get('xpath')

    # Geef de xpath uit
    xpath = request.args.get('xpath')

    # Geef de xpath uit
    xpath = request.args.get('xpath')

    # Geef de xpath uit
    xpath = request.args.get('xpath')

    # Geef de xpath uit
    xpath = request.args.get('xpath')

    # Geef de xpath uit
    xpath = request.args.get('xpath')

    # Geef de xpath uit
    xpath = request.args.get('xpath')

    # Geef de xpath uit
    xpath = request.args.get('xpath')

    # Geef de xpath uit
    xpath = request.args.get('xpath')

    # Geef de xpath uit
    xpath = request.args.get('xpath')

    # Geef de xpath uit
    xpath = request.args.get('xpath')

    # Geef de xpath uit
    xpath = request.args.get('xpath')

    # Geef de xpath uit
    xpath = request.args.get('xpath')

    # Geef de xpath uit
    xpath = request.args.get('xpath')

    # Geef de xpath uit
    xpath = request.args.get('xpath')

    # Geef de xpath uit
    xpath = request.args.get('xpath')

    # Geef de xpath uit
    xpath = request.args.get('xpath')

    # Geef de xpath uit
    xpath = request.args.get('xpath')

    # Geef de xpath uit
    xpath = request.args.get('xpath')