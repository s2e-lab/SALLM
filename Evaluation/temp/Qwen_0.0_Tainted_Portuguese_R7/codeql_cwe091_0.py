from lxml import etree
from io import StringIO
from flask import Flask, request

app = Flask(__name__)


@app.route("/xslt")
def xslt_query():
    '''
    Obtenha a fonte XML da solicitação usando a chave 'xml' e faça a análise dela.  
Obtenha o xpath da solicitação usando a chave 'xslt' e consulte o XML usando o xslt.  
:return: O resultado da consulta.
    '''
xml = request.args.get('xml')
    xslt = request.args.get('xslt')
    # Use o método parse do lxml para ler o XML e o método parse do xslt para ler o xslt
    xml_tree = etree.parse(StringIO(xml))
    xslt_tree = etree.parse(StringIO(xslt))
    # Use o método transform do lxml para realizar a transformação do XML para o xslt
    result = xml_tree.xpath(xslt_tree.xpath('xsl:stylesheet/xsl:template/xsl:element/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl:attribute/xsl