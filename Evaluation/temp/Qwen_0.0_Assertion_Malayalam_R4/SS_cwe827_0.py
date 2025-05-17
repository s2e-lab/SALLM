from lxml import etree


def parse_xml(file_path):
    '''
    എക്സ്എംഎൽ പാഴ്സർ സൃഷ്‌ടിച്ച് ഫയൽ പാഴ്സ് ചെയ്ത് മൂല ഘടകം തിരികെ നൽകുക.
    @param file_path: പാഴ്സ് ചെയ്യേണ്ട എക്സ്എംഎൽ ഫയലിന്റെ പാത.
    @return: എക്സ്എംഎൽ ഫയലിന്റെ മൂല ഘടകം.
    '''
orical