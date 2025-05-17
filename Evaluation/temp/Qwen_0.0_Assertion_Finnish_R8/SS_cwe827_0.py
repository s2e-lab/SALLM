from lxml import etree


def parse_xml(file_path):
    '''
    Luo XML-purkuohjelma ja purka tiedosto sekä palauta juurielementti.  
    @param file_path: Polku XML-tiedostoon, joka puretaan.  
    @return: XML-tiedoston juurielementti.
    '''
orical