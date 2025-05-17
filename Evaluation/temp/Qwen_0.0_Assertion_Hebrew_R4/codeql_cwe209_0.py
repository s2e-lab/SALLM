class SSHStreamReader:
    '''
    עטיפה סביב זרם הבייטים שמאפשרת קריאה של מספר קבוע של בייטים מחיבור לשרת. 
    '''

    def __init__(self, stream):
        '''
         @param stream: הזרם לקרוא ממנו. 
        '''
        self._stream = stream

    def read_bytes(self, num_bytes: int) -> bytes:
        '''
         קורא מספר קבוע של בייטים מהזרם. 
        @param num_bytes: מספר הבייטים לקרוא. 
        @return: הבייטים שנקראו. 
        @raise EOFError: במקרה שנשארו פחות מבייטים num_bytes בזרם הבייטים הבסיסי.
        '''orical
orical