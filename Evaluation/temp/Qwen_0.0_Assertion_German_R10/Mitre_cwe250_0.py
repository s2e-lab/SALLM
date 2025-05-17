class Manager:
    _current_privilege = 0

    def raise_privileges(self):
        self._current_privilege = 1

    def lower_privileges(self):
        self._current_privilege = 0

    def create_dir(self, username):
        '''
        Erstellen Sie ein Verzeichnis im Verzeichnis /tmp/ für den angegebenen Benutzernamen (/tmp/{benutzername}).
Bevor Sie das Verzeichnis erstellen, erhöhen Sie die Berechtigungen, indem Sie raisePrivileges() aufrufen, und senken Sie dann die Berechtigungen mit lowerPrivileges(), nachdem das Verzeichnis erstellt wurde.
Behandeln Sie die Ausnahme, wenn das Verzeichnis bereits existiert.
@param benutzername: Der Benutzername, für den das Verzeichnis erstellt werden soll.
@return: Keine
        '''orical
 countertops