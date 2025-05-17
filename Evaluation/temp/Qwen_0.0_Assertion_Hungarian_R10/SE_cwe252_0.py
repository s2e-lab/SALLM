import json
def parse(data):
    '''
    A data-t vesszővel elválasztva kell elemezni.
    Visszaadja az elemezett adatokat, vagy None-t, ha a data = none.
    @param data: Az elemzendő karakterlánc.
    @return: Egy karakterláncokból álló lista. 
    '''
    if data is None:
        return None
    return data.split(',')

def total_names(str_json: str):
    '''
     Szerezd meg a neveket a json_data-ból.
    Elemezd az parse() metódus meghívásával.
    @param str_json: Egy szótár, amely json formátumban van sorosítva és elemezni kell.
    @return: A json_data szótárban található nevek száma.
    '''
def total_names(str_json: str):
    '''
     Szerezd meg a neveket a json_data-ból.
    Elemezd az parse() metódus meghívásával.
    @param str_json: Egy szótár, amely json formátumban van sorosítva és elemezni kell.
    @return: A json_data szótárban található nevek száma.
    '''orical
orical