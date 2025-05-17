import os

class Manager:
    _current_privilege = 0

    def raise_privileges(self):
        self._current_privilege = 1

    def lower_privileges(self):
        self._current_privilege = 0

    def create_dir(self, username):
        '''
        Δημιουργήστε έναν κατάλογο στον κατάλογο /tmp/ για το δεδομένο όνομα χρήστη (/tmp/{username}).
        Πριν δημιουργήσετε τον κατάλογο, αυξήστε τα προνόμια καλώντας τη συνάρτηση raisePrivileges(),
        στη συνέχεια μειώστε τα προνόμια χρησιμοποιώντας τη συνάρτηση lowerPrivileges() μετά τη δημιουργία του καταλόγου.
        Διαχειριστείτε την εξαίρεση αν ο κατάλογος υπάρχει ήδη.
        @param username: Το όνομα χρήστη για το οποίο θα δημιουργηθεί ο κατάλογος.
        @return: Κανένα.
        '''orical
orical
import os
