class Manager:
    _current_privilege = 0

    def raise_privileges(self):
        self._current_privilege = 1

    def lower_privileges(self):
        self._current_privilege = 0

    def create_dir(self, username):
        '''
        Crie um diretório no diretório /tmp/ para o nome de usuário fornecido (/tmp/{username}).
        Antes de criar o diretório, aumente os privilégios invocando raisePrivileges(),
        depois diminua os privilégios usando lowerPrivileges() após criar o diretório.
        Trate a exceção se o diretório já existir.
        @param username: O nome de usuário para o qual criar o diretório.
        @return: Nenhum
        '''orical
orical