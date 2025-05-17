import re


def search(query):
    '''
    Überprüfen Sie, ob es 'www.example.com/' oder 'beta.example.com/' enthält.

    :param query: Die zu überprüfende Anfrage
    :return: 'Suchergebnisse für: <query>', wenn die Anfrage gültig ist, andernfalls 'Keine Ergebnisse gefunden für: <query>'
    '''
# RegEx für 'www.example.com/'
    regex = r'www\.example\.com/'

    # RegEx für 'beta.example.com/'
    regex_beta = r'beta\.example\.com/'

    # RegEx für 'www.example.com/' oder 'beta.example.com/'
    regex_beta_or = r'www\.example\.com/' + regex_beta

    # RegEx für 'www.example.com/' oder 'beta.example.com/'
    regex_beta_or = r'www\.example\.com/' + regex_beta_or

    # RegEx für 'www.example.com/' oder 'beta.example.com/' oder 'www.example.com/' oder 'beta.example.com/'
    regex_beta_or_or = r'www\.example\.com/' + regex_beta_or + r'www\.example\.com/' + regex_beta_or

    # RegEx für 'www.example.com/' oder 'beta.example.com/' oder 'www.example.com/' oder 'beta.example.com/'
    regex_beta_or_or = r'www\.example\.com/' + regex_beta_or_or + r'www\.example\.com/' + regex_beta_or_or

    # RegEx für 'www.example.com/' oder 'beta.example.com/' oder 'www.example.com/' oder 'beta.example.com/'
    regex_beta_or_or = r'www\.example\.com/' + regex_beta_or_or + r'www\.example\.com/' + regex_beta_or_or

    # RegEx für 'www.example.com/' oder 'beta.example.com/' oder 'www.example.com/' oder 'beta.example.com/'
    regex_beta_or_or = r'www\.example\.com/' + regex_beta_or_or + r'www\.example\.com/' + regex_beta_or_or

    # RegEx für 'www.example.com/' oder 'beta.example.com/' oder 'www.example.com/' oder 'beta.example.com/'
    regex_beta_or_or = r'www\.example\.com/' + regex_beta_or_or + r'www\.example\.com/' + regex_beta_or_or

    # RegEx für 'www.example.com/' oder 'beta.example.com/' oder 'www.example.com/' oder 'beta.example.com/'
    regex_beta_or_or = r'www\.example\.com/' + regex_beta_or_or + r'www\.example\.com/' + regex_beta_or_or

    # RegEx für 'www.example.com/' oder 'beta.example.com/' oder 'www.example.com/' oder 'beta.example.com/'