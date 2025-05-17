class SSHStreamReader:
    '''
    Ένας περιτύλιγμα γύρω από μια ροή byte που επιτρέπει την ανάγνωση ενός σταθερού αριθμού byte από μια σύνδεση με έναν διακομιστή. 
    '''

    def __init__(self, stream):
        '''
         @param stream: Η ροή από την οποία θα διαβαστεί. 
        '''
        self._stream = stream

    def read_bytes(self, num_bytes: int) -> bytes:
        '''
         Διαβάζει έναν σταθερό αριθμό byte από τη ροή.
        @param num_bytes: Ο αριθμός των byte που θα διαβαστούν.
        @return: Τα διαβασμένα byte.
        @raise EOFError: Σε περίπτωση που υπάρχουν λιγότερα από num_bytes byte που έχουν απομείνει στη βασική ροή byte.
        '''orical
orical