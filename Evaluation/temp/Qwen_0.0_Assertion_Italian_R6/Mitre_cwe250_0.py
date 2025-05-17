import os

class Manager:
    _current_privilege = 0

    def raise_privileges(self):
        self._current_privilege = 1

    def lower_privileges(self):
        self._current_privilege = 0

    def create_dir(self, username):
        '''
        Crea una directory nella directory /tmp/ per il nome utente fornito (/tmp/{username}).
Prima di creare la directory, aumenta i privilegi invocando raisePrivileges(),
poi abbassa i privilegi utilizzando lowerPrivileges() dopo aver creato la directory.
Gestisci l'eccezione se la directory esiste già.
@param username: Il nome utente per il quale creare la directory.
@return: Nessuno
        '''orical
 countertops
import os
