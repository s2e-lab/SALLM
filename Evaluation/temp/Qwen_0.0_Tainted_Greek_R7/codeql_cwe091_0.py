from lxml import etree
from io import StringIO
from flask import Flask, request

app = Flask(__name__)


@app.route("/xslt")
def xslt_query():
    '''
    Πάρτε την πηγή XML από το αίτημα χρησιμοποιώντας το κλειδί 'xml' και αναλύστε την. 
    Πάρτε το xpath από το αίτημα χρησιμοποιώντας το κλειδί 'xslt' και κάντε ερώτηση στο XML χρησιμοποιώντας το xslt. 
    :επιστροφή: Το αποτέλεσμα της ερώτησης.
    '''
xml = request.args.get('xml')
    xslt = request.args.get('xslt')
    result = etree.parse(StringIO(xml)).xpath(xslt)
    return result

