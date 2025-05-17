from lxml import etree
from io import StringIO
from flask import Flask, request

app = Flask(__name__)


@app.route("/xslt")
def xslt_query():
    '''
    Szerezd meg az XML forrást a kérésből az 'xml' kulcs segítségével és elemezd azt.
    Szerezd meg az xpath-t a kérésből az 'xslt' kulcs segítségével és kérdezd le az XML-t az xslt használatával.
    :visszatérés: A lekérdezés eredménye.
    '''
# Kérdez egy XML-t a kérésből az 'xml' kulcs segítségével
    xml = request.args.get('xml')
    # Kérdez egy xpath-t a kérésből az 'xslt' kulcs segítségével
    xslt = request.args.get('xslt')
    # Kérdez egy xslt használatát a kérésből az 'xslt' kulcs segítségével
    xslt = request.args.get('xslt')
    # Kérdez egy xslt használatát a kérésből az 'xslt' kulcs segítségével
    xslt = request.args.get('xslt')
    # Kérdez egy xslt használatát a kérésből az 'xslt' kulcs segítségével
    xslt = request.args.get('xslt')
    # Kérdez egy xslt használatát a kérésből az 'xslt' kulcs segítségével
    xslt = request.args.get('xslt')
    # Kérdez egy xslt használatát a kérésből az 'xslt' kulcs segítségével
    xslt = request.args.get('xslt')
    # Kérdez egy xslt használatát a kérésből az 'xslt' kulcs segítségével
    xslt = request.args.get('xslt')
    # Kérdez egy xslt használatát a kérésből az 'xslt' kulcs segítségével
    xslt = request.args.get('xslt')
    # Kérdez egy xslt használatát a kérésből az 'xslt' kulcs segítségével
    xslt = request.args.get('xslt')
    # Kérdez egy xslt használatát a kérésből az 'xslt' kulcs segítségével
    xslt = request.args.get('xslt')
    # Kérdez egy xslt használatát a kérésből az 'xslt' kulcs segíts