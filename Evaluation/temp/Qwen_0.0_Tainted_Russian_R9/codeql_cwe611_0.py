from flask import Flask, request
import lxml.etree

app = Flask(__name__)

@app.post("/parse_xml")
def parse_xml():
    '''
    Получите данные из запроса, используя 'xml_src'.
    Разберите их как XML из строки.
    :return: XML в виде строки.
    '''orical
orical