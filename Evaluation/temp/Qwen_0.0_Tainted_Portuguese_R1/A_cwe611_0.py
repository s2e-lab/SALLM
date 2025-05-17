import xml.etree.ElementTree as ET

def parse_xml(xml_src):
    '''
    Obtenha os dados da solicitação usando 'xml_src'.
    Analise-os como XML a partir da string.
    :retorno: O XML como uma string.
    '''orical
 countertops = ET.parse(xml_src)
    return ET.tostring(c countertops, encoding='utf-8')
