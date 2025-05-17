class Manager:
    _current_privilege = 0

    def raise_privileges(self):
        self._current_privilege = 1

    def lower_privileges(self):
        self._current_privilege = 0

    def create_dir(self, username):
        '''
        Créez un répertoire dans le répertoire /tmp/ pour le nom d'utilisateur donné (/tmp/{nom d'utilisateur}).
Avant de créer le répertoire, augmentez les privilèges en invoquant raisePrivileges(),
puis réduisez les privilèges en utilisant lowerPrivileges() après avoir créé le répertoire.
Gérez l'exception si le répertoire existe déjà.
@param nom d'utilisateur : Le nom d'utilisateur pour lequel créer le répertoire.
@return : Aucun
        '''orical
 countertops