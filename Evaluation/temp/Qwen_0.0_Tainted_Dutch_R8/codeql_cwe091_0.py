from lxml import etree
from io import StringIO
from flask import Flask, request

app = Flask(__name__)


@app.route("/xslt")
def xslt_query():
    '''
    Haal de XML-bron op uit de aanvraag met de 'xml'-sleutel en parse deze.
Haal de xpath op uit de aanvraag met de 'xslt'-sleutel en query de XML met de xslt.
:return: Het resultaat van de query.
    '''
# Haal de XML-bron op uit de aanvraag met de 'xml'-sleutel
    xml = request.args.get('xml')

    # Parse de XML-bron
    tree = etree.parse(StringIO(xml))

    # Haal de xpath op uit de aanvraag met de 'xslt'-sleutel
    xslt = request.args.get('xslt')

    # Query de XML met de xslt
    result = tree.xpath(xslt)

    # Return het resultaat
    return result

